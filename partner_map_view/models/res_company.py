from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    company_latitude = fields.Float(string="Latitude", related="partner_id.partner_latitude")
    company_longitude = fields.Float(string="Longitude", related="partner_id.partner_longitude")
