from odoo import fields
from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    industry_id = fields.Many2one(
        comodel_name="res.industry", string="Industry"
    )

    other_industry_classification = fields.Char(string="Other Industry Classification")
