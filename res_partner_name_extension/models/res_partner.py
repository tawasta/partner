# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"

    name_extension = fields.Char('Name extension', size=128)
