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
    project_ids = fields.One2many(
        'project.project',
        'partner_id',
        string='Projects',
        help='Projects assigned to related customer',
    )
    project_count = fields.Integer(
        compute='_compute_project_count',
        string='Number of projects on customer',
        help='Number of projects on customer',
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def _compute_project_count(self):
        for partner in self:
            partner.project_count = len(partner.project_ids)

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
