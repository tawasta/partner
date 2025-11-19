# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore

class ResPartner(models.Model):
    _inherit = 'res.partner'

    user_kannatusseura = fields.Many2one("kannatusseura.model", string="Kannatusseura")

    



