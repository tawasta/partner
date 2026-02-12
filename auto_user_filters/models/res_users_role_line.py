import datetime as py_datetime

from odoo import api, models


class ResUsersRoleLine(models.Model):
    _inherit = "res.users.role.line"

    @staticmethod
    def _is_line_enabled(date_from, date_to, today):
        """Return whether a role line is enabled for the given date."""
        if date_from and date_from > today:
            return False
        if date_to and today > date_to:
            return False
        return True

    def _enabled_roles_for_users(self, users):
        """Return dict {user_id: enabled roles recordset} for given users."""
        RoleLine = self.env["res.users.role.line"].sudo()
        today = py_datetime.date.today()

        lines = RoleLine.search([("user_id", "in", users.ids)])
        enabled_lines = [
            li for li in lines if self._is_line_enabled(li.date_from, li.date_to, today)
        ]

        result = {u.id: self.env["res.users.role"] for u in users}
        for line in enabled_lines:
            result[line.user_id.id] |= line.role_id
        return result

    def _apply_role_rules(self, users, roles_scope=None):
        """Create/update/deactivate auto-managed ir.filters for users.

        If ``roles_scope`` is provided, only rules belonging to these roles are
        considered for apply/deactivate (ideal for role line create/write/unlink).
        """
        users = users.sudo()
        Rule = self.env["role.irfilter.rule"].sudo()
        IrFilters = self.env["ir.filters"].sudo()

        enabled_roles_map = self._enabled_roles_for_users(users)

        if roles_scope:
            scope_rules = Rule.search([("role_id", "in", roles_scope.ids)])
        else:
            scope_rules = Rule.search([])

        active_scope_rules = scope_rules.filtered_domain([("active", "=", True)])

        for user in users:
            enabled_roles = enabled_roles_map.get(user.id, self.env["res.users.role"])
            if roles_scope:
                enabled_roles = enabled_roles & roles_scope

            # Apply active rules for enabled roles (avoid lambda capturing loop var)
            applicable_rules = active_scope_rules.filtered_domain(
                [("role_id", "in", enabled_roles.ids)]
            )
            applicable_rule_ids = set(applicable_rules.ids)

            for rule in applicable_rules:
                company_ids = rule._user_company_ids(user)

                if not company_ids:
                    IrFilters.search(
                        [
                            ("user_id", "=", user.id),
                            ("auto_rule_id", "=", rule.id),
                        ]
                    ).write({"active": False, "is_default": False})
                    continue

                domain = rule._render_domain(user)

                vals = {
                    "name": rule.filter_name,
                    "user_id": user.id,
                    "model_id": rule.model_id.model,
                    "domain": repr(domain),
                    "context": repr({"group_by": []}),
                    "sort": repr([]),
                    "is_default": rule.is_default,
                    "action_id": rule.action_id.id or False,
                    "active": True,
                    "auto_rule_id": rule.id,
                }
                IrFilters.create_or_replace(vals)

            # Deactivate filters (only ours) not applicable anymore in this scope
            domain_filters = [
                ("user_id", "=", user.id),
                ("auto_rule_id", "!=", False),
                ("auto_rule_id", "in", scope_rules.ids),
            ]
            existing = IrFilters.search(domain_filters)

            # Avoid lambda capturing loop var by binding as default argument
            to_disable = existing.filtered(
                lambda f, ids=applicable_rule_ids: f.auto_rule_id.id not in ids
            )
            if to_disable:
                to_disable.write({"active": False, "is_default": False})

    def _refresh_for_self_scope(self):
        """Refresh filters for the users/roles touched by these lines."""
        users = self.mapped("user_id")
        roles = self.mapped("role_id")
        if users and roles:
            self._apply_role_rules(users, roles_scope=roles)

    @api.model_create_multi
    def create(self, vals_list):
        recs = super().create(vals_list)
        recs._refresh_for_self_scope()
        return recs

    def write(self, vals):
        res = super().write(vals)
        if {"date_from", "date_to", "role_id", "user_id"} & set(vals.keys()):
            self._refresh_for_self_scope()
        return res

    def unlink(self):
        users = self.mapped("user_id")
        roles = self.mapped("role_id")
        res = super().unlink()
        if users and roles:
            # Refresh filters in the removed role scope -> disables removed role filters
            self._apply_role_rules(users.sudo(), roles_scope=roles.sudo())
        return res
