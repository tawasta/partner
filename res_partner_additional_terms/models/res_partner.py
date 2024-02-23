from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    additional_term_id = fields.Many2one(
        comodel_name="res_partner_additional_terms.term", string="Additional Terms"
    )
