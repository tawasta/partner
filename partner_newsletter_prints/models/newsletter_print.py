# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class NewsletterPrint(models.Model):

    # 1. Private attributes
    _name = 'newsletter.print'

    # 2. Fields declaration
    partner = fields.Many2one('res.partner', 'Partner', domain=[('is_company', '=', True)])
    contact = fields.Many2one('res.partner', 'Contact', domain=[('is_company', '=', False)])
    amount = fields.Integer("Amount")

    contact_name = fields.Char("Contact name", compute='compute_contact_name')
    contact_street = fields.Char("Contact address", compute='compute_contact_street')
    contact_zip = fields.Char("Contact zip", compute='compute_contact_zip')
    contact_city = fields.Char("Contact city", compute='compute_contact_city')
    contact_country = fields.Char("Contact country", compute='compute_contact_country')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def compute_contact_name(self):
        for record in self:
            record.contact_name = record.contact.name

    @api.multi
    def compute_contact_street(self):
        for record in self:
            contact_street = record.contact.street

            if record.contact.street2:
             contact_street + " " + record.contact.street2

            record.contact_street = contact_street

    @api.multi
    def compute_contact_zip(self):
        for record in self:
            record.contact_zip = record.contact.zip

    @api.multi
    def compute_contact_city(self):
        for record in self:
            record.contact_city = record.contact.city

    @api.multi
    def compute_contact_country(self):
        for record in self:
            record.contact_country = record.contact.country_id

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
