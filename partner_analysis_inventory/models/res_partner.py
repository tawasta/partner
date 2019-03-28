# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    location_ids = fields.One2many(
        comodel_name='stock.location',
        inverse_name='partner_id',
        string='Locations',
    )

    quant_ids = fields.One2many(
        comodel_name='stock.quant',
        string='Quants',
        compute='_compute_quant_ids',
    )

    def _compute_quant_ids(self):
        StockQuant = self.env['stock.quant']
        for record in self:
            record.quant_ids = StockQuant.search([
                ('location_id', 'in', record.location_ids.ids),
            ])
