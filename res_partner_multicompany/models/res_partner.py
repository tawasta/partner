from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_of = fields.Many2many(
        "res.company",
        "res_company_customer_rel",
        string="Customer of",
    )

    supplier_of = fields.Many2many(
        "res.company", "res_company_supplier_rel", string="Supplier of"
    )
