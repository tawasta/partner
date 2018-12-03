# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.tools.translate import _

class sale_order(models.Model):

    _inherit = 'sale.order'

    def _make_invoice(self, order, lines, context=None):

        res = super(sale_order, self)._make_invoice(order, lines)        

        invoice_obj = self.env['account.invoice']
        values = {
            'name_extension': order.partner_id.name_extension,
        }

        invoice_obj.write([res], values)
        return res
