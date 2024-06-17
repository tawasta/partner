from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    firstname2 = fields.Char("First name 2")
