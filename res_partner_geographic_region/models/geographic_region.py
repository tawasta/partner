from odoo import fields, models


class GeographicRegion(models.Model):
    _name = "geographic.region"
    _description = "Geographic Region"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
