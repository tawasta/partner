from odoo import api
from odoo import models


class PartnerPseudonymization(models.TransientModel):
    _name = "partner.pseudonymization"
    _description = "Pseudonymize partners"

    @api.multi
    def confirm(self):
        partners = self.env["res.partner"].browse(self._context.get("active_ids"))

        for partner in partners:
            partner.pseudonymize()
