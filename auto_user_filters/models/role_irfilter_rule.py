# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.tools.safe_eval import safe_eval


class RoleIrFilterRule(models.Model):
    _name = "role.irfilter.rule"
    _description = "Auto ir.filters rule per user role"
    _order = "sequence, id"

    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    name = fields.Char(required=True)

    role_id = fields.Many2one("res.users.role", required=True, ondelete="cascade")

    model_id = fields.Many2one("ir.model", required=True, ondelete="cascade")

    filter_name = fields.Char(required=True, default="Yritys")
    is_default = fields.Boolean(default=True)
    action_id = fields.Many2one(
        "ir.actions.actions",
        help="Optional. If set, filter applies only in this action context. If empty, global for the model.",
    )

    only_leaf_companies = fields.Boolean(
        default=True,
        help="If enabled, uses only companies that are not parents (no child_ids). "
             "Example: AAA(parent) + BBB(child) -> only BBB used.",
    )

    domain_template = fields.Text(
        required=True,
        default='[("subscription_ids.company_id", "in", user_company_ids)]',
        help="Python domain template. Available variables:\n"
             "- user_company_ids: list[int]\n\n"
             "Example:\n"
             "[('subscription_ids.company_id', 'in', user_company_ids)]",
    )

    def _user_company_ids(self, user):
        companies = user.company_ids
        if self.only_leaf_companies:
            companies = companies.filtered(lambda c: not c.child_ids)
        return companies.ids

    def _render_domain(self, user):
        self.ensure_one()
        localdict = {"user_company_ids": self._user_company_ids(user)}
        return safe_eval(self.domain_template, localdict)
