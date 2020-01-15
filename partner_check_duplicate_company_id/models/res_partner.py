# -*- coding: utf-8 -*-


from odoo import api, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):

    _inherit = 'res.partner'

    def fetched_business_ids(self, parent_id):
        for business_id in self.env['res.partner'].search([]).mapped('business_id'):
            if business_id and (business_id != parent_id.business_id):
                yield business_id

    @api.onchange('business_id')
    def business_id_onchange(self):
        parent_id = self.parent_id
        if self.business_id in self.fetched_business_ids(parent_id):
            raise ValidationError(_('Business ID has to be unique!'))

    def write(self, vals):
        res = super(ResPartner, self).write(vals)
        parent_id = self.parent_id
        if self.business_id in self.fetched_business_ids(parent_id):
            raise ValidationError(_('Business ID has to be unique!'))
        return res
