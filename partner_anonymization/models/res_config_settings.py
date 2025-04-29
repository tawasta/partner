from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    partner_anonymization = fields.Boolean(
        "Partner anonymization",
        config_parameter="partner_anonymization.anonymize",
        default=False,
    )

    partner_anonymization_domain = fields.Char(
        "Anonymization domain",
        config_parameter="partner_anonymization.domain",
        help="The domain to use when anonymizing partners",
    )

    partner_anonymization_remove_delay = fields.Integer(
        "Anonymization remove delay (days)",
        config_parameter="partner_anonymization.remove_delay",
        help="How many days before auto-anonymizing partners that match the domain. "
        "Use 0 for no delay",
    )

    partner_anonymization_modification_delay = fields.Integer(
        "Anonymization modification delay (days)",
        config_parameter="partner_anonymization.modification_delay",
        help="Don't remove partners that have been modified recently. "
        "Use 0 for no delay",
    )
