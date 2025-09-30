from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    company_latitude = fields.Float(string="Latitude", default=0)
    company_longitude = fields.Float(string="Longitude", default=0)
