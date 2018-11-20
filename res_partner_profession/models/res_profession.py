# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResProfession(models.Model):

    # 1. Private attributes
    _name = 'res.profession'
    _order = 'sequence,name'

    # 2. Fields declaration
    name = fields.Char(
        string="Name",
        required=True,
        translate=True
    )
    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='res_partner_res_profession_rel',
        string='Partners',
        help='Partners with this profession',
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    _sql_constraints = [
        ('name',
         'unique(name)',
         'Please use unique profession names'),
    ]

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
