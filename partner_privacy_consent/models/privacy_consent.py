from odoo import api
from odoo import fields
from odoo import models


class PrivacyConsent(models.Model):

    _inherit = "privacy.consent"

    activity_name = fields.Char(string="Activity name", related="activity_id.name")
    partner_name = fields.Char(string="Partner name", related="partner_id.name")

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = args or []
        if name:
            args = [
                "|",
                ("activity_name", operator, name),
                ("partner_name", operator, name),
            ] + args
        return self.sudo()._search(args, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        res = []
        for record in self:
            name = "{}: {}".format(record.partner_name, record.activity_name)
            res.append((record.id, name))
        return res
