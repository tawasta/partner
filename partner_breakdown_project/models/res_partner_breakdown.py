# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartnerBreakdown(models.Model):

    _inherit = 'res.partner.breakdown'

    project_ids = fields.One2many(
        comodel_name='project.project',
        inverse_name='partner_id',
        string='Projects',
    )
