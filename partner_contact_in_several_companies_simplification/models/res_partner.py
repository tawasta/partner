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
    other_contact_role = fields.Char('Positions', compute='_compute_other_contact_role')
    other_contact_function = fields.Char('Function', compute='_compute_other_contact_function')
    other_contact_phone = fields.Char('Phone', compute='_compute_other_contact_phone')
    other_contact_email = fields.Char('Email', compute='_compute_other_contact_email')

    contact_id_street = fields.Char('Street')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def _compute_other_contact_role(self):
        for record in self.sorted(key=lambda r: r.parent_id):
            result = ''

            contacts = record + record.other_contact_ids

            for contact in contacts:
                contact_name = contact.parent_id.name or ''
                result += "%s" % contact_name

                if len(contact.category_id) != 0 and contact.parent_id:
                    result += " - "

                first = True
                for category in contact.category_id.sorted(key=lambda r: r.name):
                    if first:
                        result += '%s' % category.name
                        first = False
                        continue

                    result += ', %s' % category.name

                if not first:
                    result += "\n"
            record.other_contact_role = result

    @api.multi
    def _compute_other_contact_function(self):
        for record in self.sorted(key=lambda r: r.parent_id):
            record.other_contact_function = record._compute_other_contact_field('function')

    @api.multi
    def _compute_other_contact_phone(self):
        for record in self.sorted(key=lambda r: r.parent_id):
            record.other_contact_phone = record._compute_other_contact_field('phone')

    @api.multi
    def _compute_other_contact_email(self):
        for record in self.sorted(key=lambda r: r.parent_id):
            record.other_contact_email = record._compute_other_contact_field('email')

    def _compute_other_contact_field(self, field):
        result = ''

        contacts = self + self.other_contact_ids

        for contact in contacts:
            if not getattr(contact, field):
                continue

            contact_name = contact.parent_id.name or contact.name
            result += "%s - %s\n" % (contact_name, getattr(contact, field))

        return result

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
