from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    senator_number = fields.Char(
        help="Senator number",
    )
