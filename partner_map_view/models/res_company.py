from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    company_latitude = fields.Float(string="Latitude", default=0)
    company_longitude = fields.Float(string="Longitude", default=0)
