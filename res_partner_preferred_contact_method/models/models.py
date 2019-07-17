from odoo import models, fields, api

class contact_method(models.Model):
    _name = 'res.contact_method'

    _sql_constraints = [
        ('name',
         'unique(name)',
         'Please use unique contact method names'),
    ]

    name = fields.Char(
        string="Name",
        required=True,
        translate=True,
    )
