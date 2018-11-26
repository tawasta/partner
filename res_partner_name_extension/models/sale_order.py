# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.tools.translate import _

class sale_order(models.Model):

    _inherit = 'sale.order'

    def _make_invoice(self, cr, uid, order, lines, context=None):

        res = super(sale_order, self)._make_invoice(cr, uid, order, lines)        

        invoice_obj = self.pool.get('account.invoice')
        values = {
            'name_extension': order.partner_id.name_extension,
        }

        invoice_obj.write(cr, uid, [res], values)
        return res


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
