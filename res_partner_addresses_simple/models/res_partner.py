##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2021- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################
# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import _, api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):
    # 1. Private attributes
    _inherit = "res.partner"

    # 2. Fields declaration
    type = fields.Selection(selection_add=[("other", _("Company"))])

    contact_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Contacts",
        domain=[
            ("active", "=", True),
            ("type", "=", "contact"),
            ("is_company", "=", False),
        ],
    )

    address_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Addresses",
        domain=[
            ("active", "=", True),
            "|",
            ("type", "!=", "contact"),
            ("is_company", "=", True),
        ],
    )

    # 3. Default methods

    # 4. Compute and search fields

    # 5. Constraints and onchanges
    @api.onchange("type")
    def onchange_type_update_company_type(self):
        for record in self:
            if record.type != "contact":
                record.company_type = "company"
            elif record.type == "contact" and record.parent_id:
                record.company_type = "person"

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        if "type" in vals:
            vals = self._get_address_type(vals)

        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if "type" in vals:
            vals = self._get_address_type(vals)

        return super(ResPartner, self).write(vals)

    # 7. Action methods
    def action_open_partner(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
            "flags": {"form": {"action_buttons": True}},
        }

    # 8. Business methods
    def _get_address_type(self, vals):
        address_type = vals.get("type", False)
        if len(self) > 1:
            return vals

        has_vat = bool(self.vat) or "vat" in vals and vals["vat"]

        if address_type == "contact":
            if has_vat:
                vals["is_company"] = True
                vals["company_type"] = "company"
        elif address_type == "other":
            vals["is_company"] = True
            vals["company_type"] = "company"
        else:
            vals["is_company"] = False
            vals["company_type"] = "person"

        return vals
