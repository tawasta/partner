# -*- coding: utf-8 -*-
from openerp import models, api, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_of = fields.Many2many('res.company', string='Customer of')
    supplier_of = fields.Many2many('res.company', string='Supplier of')