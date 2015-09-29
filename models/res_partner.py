# -*- coding: utf-8 -*-
from openerp import models, api, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_of = fields.Many2many('res.company', 'res_company_customer_rel', string='Customer of')
    supplier_of = fields.Many2many('res.company', 'res_companyp_supplier_rel', string='Supplier of')