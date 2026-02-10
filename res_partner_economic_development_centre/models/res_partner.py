from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    economic_development_centre_id = fields.Many2one(
        comodel_name="economic.development.centre", string="Economic Development Centre"
    )
