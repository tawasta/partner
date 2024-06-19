from odoo import fields, models


class ResEducationLevel(models.Model):
    _name = "res.education.level"
    _description = "Education level"

    name = fields.Char(string="Education level")
