from odoo import _, api, exceptions, models


class PartnerPseudonymization(models.TransientModel):
    _name = "partner.pseudonymization"

    @api.multi
    def confirm(self):
        partners = self.env["res.partner"].browse(self._context.get("active_ids"))

        for partner in partners:
            partner.pseudonymize()
