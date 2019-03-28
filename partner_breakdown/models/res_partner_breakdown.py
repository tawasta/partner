# -*- coding: utf-8 -*-
from odoo import models


class ResPartnerBreakdown(models.Model):

    _name = 'res.partner.breakdown'

    _inherits = {'res.partner': 'partner_id'}
