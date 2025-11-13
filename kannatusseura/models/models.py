# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
 
    kannatusseura_name = fields.Selection(
        string="Kannatusseura Name",
        store=True,
        selection=[],
    )

    kannatusseura_code = fields.Char(
        string="Kannatusseura Code"
    )

    kan_cat = fields.Many2one('kannatusseura.cat', string="Kannatusseura cat")


    @api.onchange('kan_cat')
    def _onchange_sport(self):
        print("moi")



