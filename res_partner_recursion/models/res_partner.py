# -*- coding: utf-8 -*-
from openerp import models, api, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    ''' NOTE: this function might be pretty heavy to
    run with large customer bases '''

    ''' TODO: optimization '''
    def _get_recursive_child_ids(self, record):
        child_ids = []

        for child in self.search([('parent_id', '=', record.id)]):
            child_ids.append(child.id)

            if self.search([('parent_id', '=', child.id)]):
                child_ids += self._get_recursive_child_ids(child)

        return child_ids

    @api.one
    def _get_recursive_parent(self):
        if self.parent_id:
            res = self.parent_id._get_recursive_parent()[0]
        else:
            res = self

        return res