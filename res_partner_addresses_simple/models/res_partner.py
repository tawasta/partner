from odoo import fields, models


class ResPartner(models.Model):
    # 1. Private attributes
    _inherit = "res.partner"

    # 2. Fields declaration
    contact_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Contacts",
        domain=[("type", "in", ["contact", "other"])],
    )

    address_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name="parent_id",
        string="Addresses",
        domain=[("type", "not in", ["contact", "other"])],
    )

    # 3. Default methods

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods

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
