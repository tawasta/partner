from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    factoring_contract_id = fields.Many2one(
        comodel_name="factoring.contract",
        string="Factoring Contract",
    )

    @api.model_create_multi
    def create(self, vals_list):
        moves = super().create(vals_list)
        for move, vals in zip(moves, vals_list, strict=True):
            if (
                "factoring_contract_id" not in vals
                and move.partner_id.factoring_contract_id
            ):
                move.factoring_contract_id = move.partner_id.factoring_contract_id
                move._onchange_factoring_contract_id()
        return moves

    @api.onchange("partner_id")
    def _onchange_partner_id_factoring_contract(self):
        for move in self:
            move.factoring_contract_id = move.partner_id.factoring_contract_id

    @api.onchange("factoring_contract_id")
    def _onchange_factoring_contract_id(self):
        for move in self:
            contract = move.factoring_contract_id
            if contract.bank_account_id:
                move.partner_bank_id = contract.bank_account_id

            if contract.free_text and not move.narration:
                move.narration = contract.free_text
