# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountInvoice(models.Model):

    # 1. Private attributes
    _inherit = 'account.invoice'

    _FIELD_STATES = {
        'draft': [('readonly', False)],
    }

    # 2. Fields declaration
    invoice_transmit_type = fields.Selection(
        'get_invoice_transmit_types',
        'Invoice transmit',
        help='Manual - No automated sending. The invoice has to be sent via mail.' + '\n' +
        'Email - No automated sending. The invoice has to be sent via email.' + '\n' +
        'eInvoice - Electronic invoice. Can be sent only to companies.' + '\n' +
        'Printed eInvoice - Electronic invoice printed to paper at the post office.' + ' ' +
        'Can be sent to individuals and companies.',
        readonly=True,
        states=_FIELD_STATES,
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def get_invoice_transmit_types(self):
        invoice_transmit_types = [
            ('manual', _('Manual')),
            ('email', _('Email')),
            ('einvoice', _('eInvoice')),
            ('paper', _('Printed eInvoice')),
        ]

        return invoice_transmit_types

    # 5. Constraints and onchanges
    @api.one
    @api.depends('partner_id')
    @api.onchange('partner_shipping_id')
    def onchange_partner_shipping_id(self):
        self.invoice_transmit_type = self.partner_id.invoice_transmit_type

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
