# -*- coding: utf-8 -*-
from odoo import api, models, fields
from odoo.tools.translate import _
import logging
_logger = logging.getLogger(__name__)


class ReferenceRight(models.Model):
    _name = "res.partner.reference_right"
    _order = "company_id, code"

    name = fields.Char(string='Reference right', size=128, translate=True)
    code = fields.Char(string='Code', size=128)
    company_id = fields.Many2one('res.company', 'Company')
    partner_ids = fields.Many2many('res.partner', id1='referenceright',
                                   id2='partner_id', string='Partners')
    # When module is installed, fetch all companies and create reference rights

    @api.model
    def _init_reference_rights(self):
        ref_rights = {
            'reference_right_allowed': _('Allowed'),
            'reference_right_ask': _('Ask'),
            'reference_right_no': _('No Right'),
        }

        company_obj = self.env['res.company']
        refright_obj = self.env['res.partner.reference_right']

        companies = company_obj.sudo().search([], order='id')

        for company in companies:
            for key, value in ref_rights.iteritems():
                vals = {'code': key, 'name': value, 'company_id': company.id}
                refright_obj.sudo().create(vals)

        return True

    @api.model
    def name_get(self):
        # Decide if there is more than one company
        company_obj = self.env['res.company']
        company_count = company_obj.sudo().search_count([])

        res = []
        for record in self.browse([]):
            name = ''

            if record.company_id.name and company_count > 1:
                name += '%s - ' % (record.company_id.name)

            name += '%s' % (record.name)

            res.append((record.id, name))

        return res

    @api.model
    def name_search(self, args, name, operator='ilike', limit=20):
        if args:
            try:
                refright_ids = args[0][2]
                refrights = self.browse([refright_ids])

                company_ids = []
                for refright in refrights:
                    company_ids.append(refright.company_id.id)

                args = [('company_id', 'not in', company_ids)]
            except IndexError:
                # No refright ids
                pass

        if not args:
            args = []
        if name:
            ids = self.search(['|', ('name', operator, name),
                               ('company_id.name', operator, name)] +
                              args, limit=limit)
        else:
            ids = self.search([] + args, limit=limit)

        return self.name_get(ids)

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if args and 0 in args and 2 in args[0]:
            refright_ids = args[0][2]
            refrights = self.browse([refright_ids])

            company_ids = []
            for refright in refrights:
                company_ids.append(refright.company_id.id)

            args = [('company_id', 'not in', company_ids)]

        return super(ReferenceRight, self).search([] + args, offset, limit,
                                                  order, count=count)

    _sql_constraints = [
        ('company_code_unique', 'unique(company_id, code)',
         'This company already has a reference right with this code.')
    ]
