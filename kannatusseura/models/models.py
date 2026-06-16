import logging

from odoo import _, api, fields, models  # type: ignore
from odoo.exceptions import UserError  # type: ignore


class ResPartner(models.Model):
    _inherit = "res.partner"

    user_kannatusseura = fields.Many2one("kannatusseura.model", string="Kannatusseura")

    def write(self, vals):
        if "title" in vals:
            new_title = vals.get("title")
            if not new_title:
                forbidden = self.filtered(lambda r: bool(r.title))
                if forbidden:
                    raise UserError("Et voi poistaa otsikkoa tältä kontaktilta.")
        return super().write(vals)

    @api.model
    def send_kannatusseura_reminder(self):
        partners = self.search([("user_kannatusseura", "=", False)])

        if not partners:
            return

        for partner in partners:
            partner.message_post(
                body="Reminder: This contact does not have a Kannatusseura assigned.",
                subject="Kannatusseura Reminder",
                message_type="notification",
                subtype_xmlid="mail.mt_note",
            )
        return True
