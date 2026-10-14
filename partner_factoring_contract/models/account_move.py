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

    def write(self, vals):
        for move in self:
            if "factoring_contract_id" in vals and not vals["factoring_contract_id"]:
                # Remove the factoring contract free text from the narration
                # We are doing this in write instead of onchange, because
                # we need to access the old factoring contract free text
                old_contract_id = move.factoring_contract_id
                move.narration = move.narration.replace(old_contract_id.free_text, "")
        res = super().write(vals)

        return res

    @api.onchange("partner_id")
    def _onchange_partner_id_factoring_contract(self):
        for move in self:
            move.factoring_contract_id = move.partner_id.factoring_contract_id

    @api.onchange("factoring_contract_id")
    def _onchange_factoring_contract_id(self):
        for move in self:
            contract = move.factoring_contract_id
            if contract:
                # Change bank account
                if contract.bank_account_id:
                    move.partner_bank_id = contract.bank_account_id

                # Add free text to narration if not already present
                free_text = contract.free_text
                if free_text and free_text not in move.narration:
                    move.narration = f"{move.narration}\n{free_text}"
            else:
                # Set the default bank account
                move._compute_partner_bank_id()

    def _get_alerts(self):
        alerts = super()._get_alerts()

        if self.factoring_contract_id and not self.is_move_sent:
            alerts["account_factoring_contract"] = {
                "level": "info",
                "message": self.env._(
                    "The invoice will be sent to %s for factoring",
                    self.factoring_contract_id.name,
                ),
            }

        return alerts
