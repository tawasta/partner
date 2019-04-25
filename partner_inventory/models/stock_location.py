# -*- coding: utf-8 -*-
from odoo import models


class StockLocation(models.Model):

    _inherit = 'stock.location'

    def action_open_quants(self):
        # Show all quants
        self.ensure_one()

        action = self.env['ir.actions.act_window'].for_xml_id(
            'stock',
            'product_open_quants',
        )

        action.update(
            target='new',
            context=dict(
                self.env.context,
            ),
            domain=[('location_id', '=', self.id)],
        )

        return action
