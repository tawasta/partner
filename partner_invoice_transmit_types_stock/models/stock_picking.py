# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class StockPicking(models.Model):
    
    # 1. Private attributes
    _inherit = 'stock.picking'

    # 2. Fields declaration
    invoice_transmit_type = fields.Char("Invoice transmit", compute='compute_invoice_transmit_type')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def compute_invoice_transmit_type(self):
        for record in self:
            if not record.partner_id.invoice_transmit_type:
                continue

            record.invoice_transmit_type = dict(
                record.partner_id.fields_get(['invoice_transmit_type'])
                ['invoice_transmit_type']['selection'])[record.partner_id.invoice_transmit_type]

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
