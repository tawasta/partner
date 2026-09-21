from odoo import fields, models


class FactoringContract(models.Model):
    _name = "factoring.contract"
    _description = "Factoring Contract"
    _rec_name = "name"

    name = fields.Char(required=True)
    identifier = fields.Char(
        required=True,
        help="Factoring agreement identifier, as agreed with the factoring company.",
    )
    type_code = fields.Char(
        help="Factoring type code, as required by the factoring company or "
        "e-invoicing operator.",
    )
    bank_account_id = fields.Many2one(
        comodel_name="res.partner.bank",
        string="Bank Account",
        help="The bank account factoring payments are collected to.",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(default=True)
