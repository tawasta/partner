
# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models, api

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):

    _inherit = 'res.partner'

    full_name = fields.Char(
        string='Full name',
        compute='_compute_full_name',
        index=True,
        store=True,
    )

    @api.multi
    @api.depends('name', 'parent_id')
    def _compute_full_name(self):
        for record in self:
            name = self._get_recursive_name(record)
            record.full_name = name

    def _get_recursive_name(self, record):
        # Returns a recursive partner name
        if record.parent_id:
            name = "%s, %s" % \
                   (self._get_recursive_name(record.parent_id), record.name)
        else:
            name = record.name

        return name
