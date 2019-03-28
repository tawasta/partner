# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        related='task_ids.timesheet_ids',
        string='Timesheets',
    )
