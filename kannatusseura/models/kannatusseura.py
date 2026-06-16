import logging

from odoo import api, fields, models  # type: ignore
from odoo.exceptions import ValidationError  # type: ignore


class KannatusseuraModel(models.Model):
    _name = "kannatusseura.model"
    _description = "Kannatusseura Model"
    _rec_name = "kannatusseura_name"
    _rec_code = "kannatusseura_code"

    _sql_constraints = [
        (
            "unique_code_unique",
            "unique(kannatusseura_code)",
            "Code already in use, try a different one.",
        )
    ]

    kannatusseura_name = fields.Char(string="Kannatusseura Name", required=True)

    kannatusseura_code = fields.Char(string="Kannatusseura Code", required=True)

    kannatusseura_kategoria = fields.Many2one(
        "kannatusseura.cat", string="Kannatusseura kategoria", required=True
    )

    # Checker function to ensure unique codes
    @api.constrains("kannatusseura_code")
    def _check_unique_code(self):
        for record in self:
            if record.kannatusseura_code:
                existing = self.search(
                    [
                        ("kannatusseura_code", "=", record.kannatusseura_code),
                        ("id", "!=", record.id),
                    ],
                    limit=1,
                )
                if existing:
                    raise ValidationError(
                        "This code is already assigned to another contact."
                    )
