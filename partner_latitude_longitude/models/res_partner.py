from odoo import fields, models


class ResPartnerLatLong(models.Model):

    _inherit = "res.partner"

    latitude = fields.Float(default="0.0")
    longitude = fields.Float(default="0.0")
