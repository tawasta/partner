from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    # Pull name extension suggestion from partner info
    name_extension = fields.Char("Name extension", size=128)

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if self.partner_id and self.partner_id.name_extension:
            self.name_extension = self.partner_id.name_extension
        return super()._onchange_partner_id()
