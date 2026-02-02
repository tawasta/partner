from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    domicile = fields.Char(
        help="Domicile is the legal definition of a person's home municipality.",
    )
