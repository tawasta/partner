from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    factoring_contract_id = fields.Many2one(
        comodel_name="factoring.contract",
        string="Factoring Contract",
        help="Default factoring contract for invoices to this partner.",
    )
