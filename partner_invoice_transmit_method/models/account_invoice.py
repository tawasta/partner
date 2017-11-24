# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo import _


class AccountInvoice(models.Model):

    # 1. Private attributes
    _inherit = 'account.invoice'

    # 2. Fields declaration
    invoice_transmit_method = fields.Selection(
        selection='get_invoice_transmit_methods',
        string='Invoice transmit',
        help='Manual print - No automated sending. The invoice should be printed and sent via mail.' + '\n' +
        'Email - No automated sending. The invoice has to be sent manually via email.' + '\n' +
        'eInvoice - Electronic invoice. The recipient must have a valid eInvoice address.' + '\n' +
        'Printed eInvoice - Electronic invoice printed to paper at the post office.' + ' ' +
        'Can be sent to individuals and companies.',
        default=lambda self: self.get_default_invoice_transmit_method(),
    )

    # 3. Default methods
    @api.multi
    def get_default_invoice_transmit_method(self):
        #  TODO: create configurable default transmit method
        return 'email'

    # 4. Compute and search fields, in the same order that fields declaration
    def get_invoice_transmit_methods(self):
        invoice_transmit_methods = [
            ('manual', _('Manual print')),
            ('email', _('Email')),
            ('einvoice', _('eInvoice')),
            ('paper', _('Printed eInvoice')),
        ]

        return invoice_transmit_methods

    # 5. Constraints and onchanges
    @api.one
    @api.depends('partner_id')
    @api.onchange('partner_shipping_id')
    def onchange_partner_shipping_id(self):
        self.invoice_transmit_method = self.partner_id.invoice_transmit_method

    # 6. CRUD methods
    @api.model
    def create(self, values):
        if 'invoice_transmit_method' not in values and 'partner_id' in values:
            partner = self.env['res.partner'].browse([values['partner_id']])
            values['invoice_transmit_method'] = partner.invoice_transmit_method

        res = super(AccountInvoice, self).create(values)

        return res


    # 7. Action methods

    # 8. Business methods
