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
    other_contact_roles = fields.Char('Positions', compute='_compute_other_contact_roles')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def _compute_other_contact_roles(self):
        for record in self:
            other_roles = ''

            contacts = record + record.other_contact_ids

            for contact in contacts:
                contact_name = contact.parent_id.name or ''
                other_roles += "%s" % contact_name

                if contact.function:
                    other_roles += " - %s " % contact.function

                if len(contact.category_id) != 0 and contact.parent_id:
                    other_roles += ": "

                first = True
                for category in contact.category_id:
                    if first:
                        other_roles += '%s' % category.name
                        first = False
                        continue

                    other_roles += ', %s' % category.name

                other_roles += "\n\n"
            record.other_contact_roles = other_roles

    # 5. Constraints and onchanges
    @api.onchange('name')
    def onchange_name(self):
        if self.contact_id:
            # Update the main contact (if modifying child)
            self.contact_id.name = self.name

        if self.other_contact_ids:
            # Update child contact (if modifying parent)
            self.other_contact_ids.write({'name': self.name})

    # 6. CRUD methods
    @api.multi
    def write(self, values):
        for record in self:
            # Update parents children contact names
            if record.other_contact_ids and 'name' in values:
                record.other_contact_ids.write({'name': values['name']})

        return super(ResPartner, self).write(values)

    # 7. Action methods

    # 8. Business methods
