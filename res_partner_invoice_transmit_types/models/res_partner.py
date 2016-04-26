# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    invoice_transmit_type = fields.Selection(
        'get_invoice_transmit_types',
        'Invoice transmit',
        help='Default value for how the invoice is sent to the recipient.' + '\n' +
        'This can be overriden for each invoice as needed.' + '\n\n' +

        'Manual - No automated sending. The invoice has to be sent via mail.' + '\n' +
        'Email - No automated sending. The invoice has to be sent via email.' + '\n' +
        'eInvoice - Electronic invoice. Can be sent only to companies.' + '\n' +
        'Printed eInvoice - Electronic invoice printed to paper at the post office.' + ' ' +
        'Can be sent to individuals and companies.')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def get_invoice_transmit_types(self):
        return self.env['account.invoice'].get_invoice_transmit_types()

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
