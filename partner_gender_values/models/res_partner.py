from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    gender = fields.Selection(
        selection_add=[
            (
                "not_to_say",
                ("I prefer not to say"),
            )
        ]
    )
