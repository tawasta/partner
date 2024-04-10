from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    guardian_ids = fields.Many2many(
        "res.partner",
        "res_partner_guardian_relation",
        "guardians",
        "wards",
        string="Ward of",
        domain=[("is_company", "=", False), ("partner_share", "=", True)],
    )
    ward_ids = fields.Many2many(
        "res.partner",
        "res_partner_guardian_relation",
        "wards",
        "guardians",
        string="Guardian of",
        domain=[("is_company", "=", False), ("partner_share", "=", True)],
    )
