
from odoo import models, fields
from odoo.tools.translate import _

class partner(models.Model):

    _inherit = "res.partner"


    name_extension = fields.Char('Name extension', size=128)
