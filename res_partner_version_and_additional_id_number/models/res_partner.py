from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    version_number = fields.Integer(string="Version", copy=False)

    id_number_info = fields.Integer(string="ID info", copy=False)
