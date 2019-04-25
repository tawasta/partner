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

    quant_count = fields.Integer(
        string='Quants',
        compute='_compute_quant_count',
    )

    def _compute_quant_ids(self):
        StockQuant = self.env['stock.quant']
        for record in self:
            record.quant_ids = StockQuant.search([
                ('location_id', 'in', record.location_ids.ids),
            ])

    def _compute_quant_count(self):
        for partner in self:
            partner.quant_count = len(partner.quant_ids)

    def action_open_quants(self):
        # Show all quants
        self.ensure_one()

        action = self.env['ir.actions.act_window'].for_xml_id(
            'stock',
            'product_open_quants',
        )

        action.update(
            context=dict(
                self.env.context,
                search_default_locationgroup=True,
            ),
            domain=[('location_id', 'in', self.location_ids.ids)],
        )

        return action
