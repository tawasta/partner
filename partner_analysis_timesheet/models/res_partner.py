from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        compute='_compute_timesheet_ids',
        string='Timesheets',
    )

    def _compute_timesheet_ids(self):
        AnalyticLine = self.env['account.analytic.line']
        for record in self:
            record.timesheet_ids = AnalyticLine.search([
                ('task_id', 'in', record.task_ids.ids),
            ])
