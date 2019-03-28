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
        related='location_ids.quant_ids',
    )
