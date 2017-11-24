# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    invoice_transmit_method = fields.Selection(
        selection='get_invoice_transmit_methods',
        string='Invoice transmit',
        help='Manual print - No automated sending. The invoice should be printed and sent via mail.' + '\n' +
        'Email - No automated sending. The invoice has to be sent manually via email.' + '\n' +
        'eInvoice - Electronic invoice. The recipient must have a valid eInvoice address.' + '\n' +
        'Printed eInvoice - Electronic invoice printed to paper at the post office.' + ' ' +
        'Can be sent to individuals and companies.',
        default=lambda self: self.env['account.invoice'].get_default_invoice_transmit_method(),
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def get_invoice_transmit_methods(self):
        return self.env['account.invoice'].get_invoice_transmit_methods()

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
