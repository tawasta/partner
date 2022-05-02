from odoo import fields, models


class Partner(models.Model):

    _inherit = "res.partner"

    accepted_privacy_consent_ids = fields.One2many(
        comodel_name="privacy.consent",
        inverse_name="partner_id",
        string="Accepted privacy consents",
        domain=[("accepted", "=", True)],
    )
