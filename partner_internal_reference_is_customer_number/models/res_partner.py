from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    ref = fields.Char(string="Customer Number", index=True)
