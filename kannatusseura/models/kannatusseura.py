from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class KannatusseuraCategory(models.Model):
    _name = "kannatusseura.category"


    name = fields.Char(string="Nimi")
    code = fields.Char(String="Koodi")


    @api.constrains("code")
    def _check_unique_code(self):
        for record in self:
            if record.code:
                existing = self.search([("code", '=', record.code),
                                        ('id', '!=', record.id)
                                        ], limit=1)
                if existing:
                    raise ValidationError("Koodi '%s' on jo olemassa Kategoriassa, sen täytyy olla uniikki" % record.code)


class KannatusSeura(models.Model):
    _name = "kannatusseura.kannatusseura"
    _order = "name ASC"

    name = fields.Char(string="Nimi")
    category_id = fields.Many2one("kannatusseura.category", string="Kategoria")
    code = fields.Char(String="Koodi")

    @api.constrains("code")
    def _check_unique_code(self):
        for record in self:
            if record.code:
                existing = self.search([("code", '=', record.code),
                                        ('id', '!=', record.id)
                                        ], limit=1)
                if existing:
                    raise ValidationError("Koodi '%s' on jo olemassa Kannatusseurassa, sen täytyy olla uniikki" % record.code)

# Shows contacts club information in the profile
class ResPartner(models.Model):
    _inherit = "res.partner"

    kannatusseura_id = fields.Many2one('kannatusseura.kannatusseura', string="Kannatusseura")


#Sends message to contacts without contact club information
class KannatusseuraCron(models.Model):
    _name = "kannatusseura.cron"

    @api.model
    def check_missing_kannatusseura(self):
        partners = self.env["res.partner"].search([("kannatusseura_id", "=", False)])
        for partner in partners:
            partner.message_post(
                body="Tällä kontaktilla ei ole kannatusseura-arvoa",
                subtype_xmlid="mail.mt_note"
            )
        return True
