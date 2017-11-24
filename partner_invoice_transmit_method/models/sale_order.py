# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):

    # 1. Private attributes
    _inherit = 'sale.order'

    _FIELD_STATES = {
        'draft': [('readonly', False)],
        'sent': [('readonly', False)],
        'manual': [('readonly', False)],
    }
    help_text = lambda self: self.env['account.invoice'].get_invoice_transmit_method_help()

    # 2. Fields declaration
    invoice_transmit_method = fields.Selection(
        selection='get_invoice_transmit_methods',
        string='Invoice transmit',
        help='Manual print - No automated sending. The invoice should be printed and sent via mail.' + '\n' +
        'Email - No automated sending. The invoice has to be sent manually via email.' + '\n' +
        'eInvoice - Electronic invoice. The recipient must have a valid eInvoice address.' + '\n' +
        'Printed eInvoice - Electronic invoice printed to paper at the post office.' + ' ' +
        'Can be sent to individuals and companies.',
        readonly=True,
        states=_FIELD_STATES,
        default=lambda self: self.env['account.invoice'].get_default_invoice_transmit_method(),
    )

    # 3. Default methods

    # 4. Compute and search fields
    def get_invoice_transmit_methods(self):
        return self.env['account.invoice'].get_invoice_transmit_methods()

    # 5. Constraints and onchanges
    @api.multi
    @api.onchange('partner_id')
    def update_invoice_transmit_method(self):
        for record in self:
            if record.partner_id:
                record.invoice_transmit_method = record.partner_id.invoice_transmit_method

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def _make_invoice(self, order, lines):
        res = super(SaleOrder, self)._make_invoice(order, lines)
        invoice = self.env['account.invoice'].browse(res)
        invoice.invoice_transmit_method = order.invoice_transmit_method

        return res
