# -*- coding: utf-8 -*-
from openerp import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    note_ids = fields.One2many("res.partner.note", 'partner_id',
                               'Internal notes')
