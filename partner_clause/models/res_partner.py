from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    invoice_clause = fields.Many2one(
        "partner.clause",
        string="Invoice clause",
        copy=False,
        default=False,
        domain=[("used_for", "=", "invoice")],
    )

    sale_clause = fields.Many2one(
        "partner.clause",
        string="Sale clause",
        copy=False,
        default=False,
        domain=[("used_for", "=", "sale")],
    )
