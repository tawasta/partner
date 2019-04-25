# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    project_ids = fields.One2many(
        comodel_name='project.project',
        inverse_name='partner_id',
        string='Projects',
    )

    def action_open_tasks(self):
        # Show all tasks
        self.ensure_one()

        action = self.env['ir.actions.act_window'].for_xml_id(
            'project',
            'action_view_task',
        )

        action.update(
            target='new',
            context=dict(
                self.env.context,
                search_default_Stage=True,
            ),
            domain=[('project_id', 'in', self.project_ids.ids)],
        )

        return action
