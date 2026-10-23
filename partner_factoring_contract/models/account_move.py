from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    factoring_contract_id = fields.Many2one(
        comodel_name="factoring.contract",
        string="Factoring Contract",
        tracking=True
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
        return moves

    @api.onchange("partner_id")
    def _onchange_partner_id_factoring_contract(self):
        for move in self:
            move.factoring_contract_id = move.partner_id.factoring_contract_id
