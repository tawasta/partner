# -*- coding: utf-8 -*-
from openerp import models, api, fields


class InternalNote(models.Model):
    _name = "res.partner.note"
    _order = "create_date desc"

    active = fields.Boolean("Active", default=True)
    name = fields.Char("Title", size=256)
    note = fields.Text("Note")
    partner_id = fields.Many2one("res.partner", "Partner")

    @api.multi
    def unlink(self):
        ''' Deactivates the note instead of deleting '''

        self.active = False

        return True
