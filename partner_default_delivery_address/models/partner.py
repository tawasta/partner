from odoo import api
from odoo import fields
from odoo import models


class Partner(models.Model):

    _inherit = "res.partner"

    default_partner_delivery_id = fields.Many2one(
        comodel_name="res.partner", string="Default delivery address"
    )

    @api.multi
    def address_get(self, adr_pref=None):
        res = super(Partner, self).address_get(adr_pref)

        for record in self:
            if res.get("delivery") and record.default_partner_delivery_id:
                res["delivery"] = record.default_partner_delivery_id.id

        return res
