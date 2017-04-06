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
    business_segment = fields.Many2one('business_segment.segment', string='Business Segment')
    business_segment_subsegment = fields.Many2one(
        'business_segment.segment',
        string='Business sub-segment'
    )

    business_size = fields.Many2one('business_size.size', string='Business Size')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.multi
    @api.onchange("business_segment")
    def onchange_business_segement_clear_subsegment(self):
        for record in self:
            record.business_segment_subsegment = False

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
