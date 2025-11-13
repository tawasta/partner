# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
 
    kannatusseura_name = fields.Char(
        string="Kannatusseura Name"
    )

    kannatusseura_code = fields.Char(
        string="Kannatusseura Code"
    )

    kan_kat = fields.Many2one('kannatusseura.category', string="Kannatusseura category")

