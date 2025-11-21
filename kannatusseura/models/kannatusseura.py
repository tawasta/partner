from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
import logging

_logger = logging.getLogger(__name__)

class KannatusseuraCategory(models.Model):
    _name = "kannatusseura.category"


    name = fields.Char(string="Nimi")
    code = fields.Char(String="Koodi")


    _sql_constraints = [
        ('unique_code_category',
         'unique(code)',
         "Koodi on jo olemassa Kategoriassa, sen täytyy olla uniikki."),
    ]

class KannatusSeura(models.Model):
    _name = "kannatusseura.kannatusseura"
    _order = "name ASC"

    name = fields.Char(string="Nimi")
    category_id = fields.Many2one("kannatusseura.category", string="Kategoria")
    code = fields.Char(String="Koodi")

    _sql_constraints = [
        ('unique_code_kannatusseura',
         'unique(code)',
         "Koodi on jo olemassa Kannatusseurassa, sen täytyy olla uniikki."),
    ]

# Shows contacts club information in the profile
class ResPartner(models.Model):
    _inherit = "res.partner"

    kannatusseura_id = fields.Many2one('kannatusseura.kannatusseura', string="Kannatusseura")
    @api.model
    def check_missing_kannatusseura(self):
        partners = self.env["res.partner"].search([("kannatusseura_id", "=", False)])
        for partner in partners:
            partner.message_post(
                body="Tällä kontaktilla ei ole kannatusseura-arvoa",
                subtype_xmlid="mail.mt_note"
            )
        return True


    def write(self, vals):
        if "title" not in vals:
            return super(ResPartner, self).write(vals)

        new_title = vals.get("title")

        for partner in self:
            old_title = partner.title.id if partner.title else False

            if old_title and not new_title:
                raise UserError(_("Et voi poistaa otsikkoa tältä kontaktilta."))

        return super(ResPartner, self).write(vals)
    
