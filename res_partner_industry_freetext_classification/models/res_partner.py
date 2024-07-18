from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    other_industry_classification = fields.Char(string="Other Industry Classification")
