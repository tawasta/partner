# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models, api, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    type = fields.Selection(
        selection_add=[
            ('other', _('Company')),
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
        string='Addresses',
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
    @api.onchange('type')
    def onchange_type_update_company_type(self):
        for record in self:
            if record.type != 'contact':
                record.company_type = 'company'
            elif record.type == 'contact' and record.parent_id:
                record.company_type = 'person'

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def action_open_partner(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'res_model': 'res.partner',
                'view_mode': 'form',
                'res_id': self.id,
                'target': 'new',
                'flags': {'form': {'action_buttons': True}}}

    # 8. Business methods

