# -*- coding: utf-8 -*-
from openerp import fields, models, api
from openerp.exceptions import ValidationError


class ResZipGroupRange(models.Model):

    _name = 'res.zip.group.range'

    @api.constrains('start', 'end')
    def _check_range(self):
        for record in self:
            if not record.start.isdigit() or not record.end.isdigit():
                raise ValidationError('Start and end should be numeric')

            if len(record.start) != len(record.end):
                raise ValidationError('Start & end should be the same length')

    group_id = fields.Many2one(
        comodel_name='res.zip.group',
        string='Zip Group'
    )

    start = fields.Char(
        string='Start',
        required=True
    )

    end = fields.Char(
        string='End',
        required=True
    )
