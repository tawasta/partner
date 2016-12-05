# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResCompany(models.Model):

    # 1. Private attributes
    _inherit = 'res.company'

    # 2. Fields declaration
    display_name = fields.Char(compute='_get_display_name')

    # 3. Default methods
    @api.multi
    @api.depends('name', 'parent_id')
    def name_get(self):

        # Use display name instead of name
        res = []

        for record in self:
            if record.display_name:
                name = record.display_name
            else:
                name = record.name

            res.append((record.id, name))

        return res

    # 4. Compute and search fields, in the same order that fields declaration
    @api.one
    @api.depends('name', 'parent_id.name')
    def _get_display_name(self):
        # Returns a name with a complete hierarchy
        self.display_name = self._get_recursive_name(self)

    def _get_recursive_name(self, record):
        # Returns a recursive partner name

        if record.parent_id and record.parent_id.id != 1:
            record.display_name = "%s, %s"\
                % (self._get_recursive_name(record.parent_id), record.name)
        else:
            record.display_name = record.name

        return record.display_name

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
