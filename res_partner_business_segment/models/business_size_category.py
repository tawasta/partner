# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class BusinessSizeCategory(models.Model):

    # 1. Private attributes
    _name = 'business_size.category'

    # 2. Fields declaration
    name = fields.Char(string="Business size")
    business_size = fields.Char(string='Business Size')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
