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
    contact_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Contacts',
        domain=[
            ('active', '=', True),
            ('type', '=', 'contact'),
        ]
    )

    address_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Contacts',
        domain=[
            ('active', '=', True),
            ('type', '!=', 'contact'),
        ]
    )

    # 3. Default methods

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
