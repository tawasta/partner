# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        compute='_compute_timesheet_ids',
        string='Timesheets',
    )

    timesheet_count = fields.Integer(
        string='Quants',
        compute='_compute_timesheet_count',
    )

    def _compute_timesheet_ids(self):
        AnalyticLine = self.env['account.analytic.line']
        for record in self:
            record.timesheet_ids = AnalyticLine.search([
                ('task_id', 'in', record.task_ids.ids),
            ])

    def _compute_timesheet_count(self):
        for partner in self:
            partner.timesheet_count = len(partner.timesheet_ids)

    def action_open_timesheets(self):
        # Show all timesheets
        self.ensure_one()

        action = self.env['ir.actions.act_window'].for_xml_id(
            'hr_timesheet',
            'project_task_action_view_timesheet',
        )

        action.update(
            context=dict(
                self.env.context,
            ),
            domain=[('id', 'in', self.timesheet_ids.ids)],
        )

        return action
