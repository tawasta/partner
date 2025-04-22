from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    number_of_votes = fields.Integer("Number of Votes")
