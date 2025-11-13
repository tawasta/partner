from odoo import models, fields

class KannatusseuraCategory(models.Model):
    _name = 'kannatusseura.category'
    

    name = fields.Char(string="Category", required=True)
    code = fields.Char(string="Code")
