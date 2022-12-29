from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.model
    def create(self, values):
        res = super().create(values)
        res.property_account_position_id = self.env[
            "account.fiscal.position"
        ].get_fiscal_position(res.id)

        return res
