from odoo import fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    partner_customer_rank = fields.Integer(related="partner_id.customer_rank")
    partner_is_company = fields.Boolean(related="partner_id.is_company")
