# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    additional_term_id = fields.Many2one('res_partner_additional_terms.term', 'Additional Terms')