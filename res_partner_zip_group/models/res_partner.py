# -*- coding: utf-8 -*-
from openerp import fields, models, api, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    zip_group_ids = fields.Many2many(
        comodel_name='res.zip.group',
        compute='_get_zip_group_ids',
        string='ZIP Code Groups',
        store=True,
    )

    def in_zip_group(self, group):
        if self.country_id == group.country_id and self.zip \
            and self.zip in group._get_zip_codes():
            return True
        else:
            return False

    @api.depends('zip', 'country_id')
    def _get_zip_group_ids(self):
        all_zip_groups = self.env['res.zip.group'].search(args=[])

        for partner in self:
            partners_zip_group_ids = []

            for zip_group in all_zip_groups:
                if partner.in_zip_group(zip_group):
                    partners_zip_group_ids.append(zip_group.id)
            
            partner.zip_group_ids = partners_zip_group_ids
