from odoo import fields, models


class EconomicDevelopmentCentre(models.Model):
    _name = "economic.development.centre"
    _description = "Economic Development Centre"

    name = fields.Char(required=True, translate=True)
    code = fields.Char(required=True)

    active = fields.Boolean(default=True)
