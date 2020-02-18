from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _make_invoice(self, order, lines):

        res = super(SaleOrder, self)._make_invoice(order, lines)

        invoice_obj = self.env["account.invoice"]
        values = {"name_extension": order.partner_id.name_extension}

        invoice_obj.write([res], values)
        return res
