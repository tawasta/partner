from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    default_partner_invoice_id = fields.Many2one(
        comodel_name="res.partner", string="Default Invoice Address", tracking=True
    )

    def address_get(self, adr_pref=None):
        res = super().address_get(adr_pref)

        for record in self:
            if res.get("invoice") and record.default_partner_invoice_id:
                res["invoice"] = record.default_partner_invoice_id.id

        return res
