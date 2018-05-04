# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    type = fields.Selection(
        selection_add=[
            ('other', 'Company'),
        ],
    )

    contact_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Contacts',
        domain=[
            ('active', '=', True),
            ('type', '=', 'contact'),
            ('is_company', '=', False),
        ]
    )

    address_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Contacts',
        domain=[
            ('active', '=', True),
            '|',
            ('type', '!=', 'contact'),
            ('is_company', '=', True),
        ]
    )

    # 3. Default methods

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods
    def create(self, vals):
        if 'type' in vals:
            vals = self._get_address_type(vals)

        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'type' in vals:
            vals = self._get_address_type(vals)

        return super(ResPartner, self).write(vals)

    # 7. Action methods

    # 8. Business methods
    def _get_address_type(self, vals):
        address_type = vals.get('type', False)
        has_vat = bool(self.vat) or 'vat' in vals

        if address_type == 'contact':
            if has_vat:
                vals['is_company'] = True
                vals['company_type'] = 'company'
        elif address_type == 'other':
            vals['is_company'] = True
            vals['company_type'] = 'company'
        else:
            vals['is_company'] = False
            vals['company_type'] = 'person'

        return vals
