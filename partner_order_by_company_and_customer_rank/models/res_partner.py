from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"
    _order = "is_company desc, customer_rank desc"

    @api.depends("customer_rank", "is_company")
    def _compute_customer_rank_by_company(self):
        for partner in self:
            is_company = partner.is_company and 100 or 0
            partner.customer_rank_by_company = partner.customer_rank + is_company

    customer_rank_by_company = fields.Float(compute="_compute_customer_rank_by_company")
