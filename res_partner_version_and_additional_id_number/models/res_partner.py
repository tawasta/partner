from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    version_number = fields.Integer(string="Version", copy=False, store=True)

    id_number_info = fields.Integer(string="ID info", copy=False, store=True)
