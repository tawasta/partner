from odoo import models


class ResPartner(models.Model):

    _inherit = "res.partner"
    _order = "is_company, customer_rank"
