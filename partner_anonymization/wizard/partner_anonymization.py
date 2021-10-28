from odoo import models


class PartnerAnonymization(models.TransientModel):
    _name = "partner.anonymization"
    _description = "Anonymize partners"

    def confirm(self):
        partners = self.env["res.partner"].browse(self._context.get("active_ids"))

        for partner in partners:
            partner.anonymize()
