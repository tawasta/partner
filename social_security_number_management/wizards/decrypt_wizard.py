import logging

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class PartnerSSNDecryptWizard(models.TransientModel):
    _name = "partner.ssn.decrypt.wizard"
    _description = "Decrypt Partner Personal ID"

    key = fields.Char(
        string="Decryption Key",
        required=True,
        help="Base64 encoded encryption key. Ask your system administrator.",
        password=True,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)

    def decrypt_social_security_number(self):
        self.ensure_one()
        partner = self.partner_id

        if not partner.encrypted_social_security_number:
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": _("No Personal Identification Number"),
                    "message": _("No encrypted personal identification number"),
                    "sticky": False,
                },
            }

        decrypted_id = partner.decrypt_social_security_number(
            partner.encrypted_social_security_number,
            self.key,
        )

        if decrypted_id in (
            _("The key you provided is incorrect."),
            _("Decryption failed"),
        ):
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": _("Decryption failed"),
                    "message": decrypted_id,
                    "sticky": False,
                },
            }

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Decrypted Personal Identification Number"),
                "message": decrypted_id,
                "sticky": False,
            },
        }