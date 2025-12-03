from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    linkedin_url = fields.Char(
        string="LinkedIn",
        help="Partnerin LinkedIn-profiilin URL, esim. https://www.linkedin.com/in/tunnus",
    )
