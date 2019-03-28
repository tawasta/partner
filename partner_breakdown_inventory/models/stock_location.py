# -*- coding: utf-8 -*-
from odoo import fields, models


class StockLocation(models.Model):

    _inherit = 'stock.location'

    quant_ids = fields.One2many(
        comodel_name='stock.quant',
        inverse_name='location_id',
        string='Quants',
    )
