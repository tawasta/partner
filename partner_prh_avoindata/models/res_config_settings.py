from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    prh_use_industry = fields.Boolean(
        "Use industry",
        config_parameter="prh.use_industry",
        help="Fetch and create industry from PRH",
        default=True,
    )

    prh_language_code = fields.Selection(
        string="PRH language",
        selection=[
            ("1", "Finnish"),
            ("2", "Swedish"),
            ("3", "English"),
        ],
        config_parameter="prh.language",
        default="1",
        help="Which language to use for importing data",
    )
