from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_company = fields.Boolean(default=True)
