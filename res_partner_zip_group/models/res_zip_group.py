# -*- coding: utf-8 -*-
from openerp import fields, models, api


class ResZipGroup(models.Model):

    _name = 'res.zip.group'

    def _get_zip_codes(self):
        zip_codes = []
        for zip_range in self.zip_range_ids:

            numeric_start = int(zip_range.start.lstrip('0'))
            numeric_end = int(zip_range.end.lstrip('0'))

            # Fields constraints force start and end to be the same length
            length = len(zip_range.start)

            for i in range(numeric_start, numeric_end+1):
                zip_codes.append(str(i).zfill(length))

        return list(set(zip_codes))

    @api.depends('zip_range_ids', 'country_id')
    def _get_partner_ids(self):
        args = [('country_id', '=', self.country_id.id),
                ('zip', 'in', self._get_zip_codes())]
        partners = self.env['res.partner'].search(args=args)

        self.partner_ids = [p.id for p in partners]

    name = fields.Char('Name')
    description = fields.Text('Description')

    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        required=True
    )

    zip_range_ids = fields.One2many(
        comodel_name='res.zip.group.range',
        inverse_name='group_id',
        string='Zip Ranges'
    )

    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        compute='_get_partner_ids',
        string='Partners',
        store=False,
    )
