from odoo import fields
from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    education_level_id = fields.Many2one(
        comodel_name="res.education.level", string="Education level"
    )

    other_education_or_degree = fields.Char(string="Other education or degree") 
