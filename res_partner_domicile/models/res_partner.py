from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    domicile = fields.Char(
        string="Domicile",
        help="Domicile is the legal definition of a person's home municipality.",
    )
