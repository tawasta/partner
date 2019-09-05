# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class BusinessSize(models.Model):

    # 1. Private attributes
    _name = "business_size.size"
    _order = 'name'

    # 2. Fields declaration
    name = fields.Char(string='Business Size')
    category = fields.Many2one('business_size.category', string='Size Category')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
