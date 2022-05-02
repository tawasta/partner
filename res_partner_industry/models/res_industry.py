# 1. Standard library imports:
# 2. Known third party imports:
# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResIndustry(models.Model):

    # 1. Private attributes
    _name = "res.industry"
    _description = "Industry"

    # 2. Fields declaration
    name = fields.Char(string="Industry")
