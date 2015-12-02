# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class SaleOrder(models.Model):

    # 1. Private attributes
    _inherit = 'sale.order'

    # 2. Fields declaration
    invoice_transmit_type = fields.Selection([
           ('manual', 'Manual'),
           ('einvoice', 'eInvoice'),
           ('paper', 'Printed eInvoice'),
          ],
          'Invoice transmit',
          help='Manual - No automated sending. The invoice has to be sent via mail or email.' + '\n' +
               'eInvoice - Electronic invoice. Can be sent only to companies.' + '\n' +
               'Printed eInvoice - Electronic invoice printed to paper at the post office.' + ' ' +
               'Can be sent to individuals and companies.')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.one
    @api.onchange('partner_id')
    def update_invoice_transmit_type(self):
        if self.partner_id:
            self.invoice_transmit_type = self.partner_id.invoice_transmit_type

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def _make_invoice(self, order, lines):
        res = super(SaleOrder, self)._make_invoice(order, lines)
        invoice = self.env['account.invoice'].browse(res)
        invoice.invoice_transmit_type = order.invoice_transmit_type

        return res
