from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    name_extension = fields.Char("Name extension", size=128)
