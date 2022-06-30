from odoo import fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    customer_number = fields.Char(related="partner_id.ref")
