# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore
import logging

class ResPartner(models.Model):
    _inherit = 'res.partner'

    user_kannatusseura = fields.Many2one("kannatusseura.model", string="Kannatusseura")


    @api.model
    def send_kannatusseura_reminder(self):
        partners = self.search([('user_kannatusseura', '=', False)])
        
        if not partners:
            return
        
        for partner in partners:

            partner.message_post(
                body="Reminder: This contact does not have a Kannatusseura assigned.",
                subject="Kannatusseura Reminder",
                message_type="notification",
                subtype_xmlid="mail.mt_note"
            )
        return True


    



