from odoo import api, fields, models  # type: ignore
from odoo.exceptions import ValidationError  # type: ignore


class KannatusseuraCat(models.Model):
    _name = "kannatusseura.cat"
    _description = "Kannatusseura Category"
    _rec_name = "kannatusseura_cat_name"

    kannatusseura_cat_name = fields.Char(string="Kannatusseura Category", required=True)
    kannatusseura_cat_code = fields.Char(string="KanCatCode", required=True)

    _sql_constraints = [
        (
            "unique_code_unique",
            "unique(kannatusseura_cat_code)",
            "Category code already in use, try a different one.",
        )
    ]

    @api.constrains("kannatusseura_cat_code")
    def _check_unique_code(self):
        for record in self:
            if record.kannatusseura_cat_code:
                existing = self.search(
                    [
                        ("kannatusseura_cat_code", "=", record.kannatusseura_cat_code),
                        ("id", "!=", record.id),
                    ],
                    limit=1,
                )
                if existing:
                    raise ValidationError(
                        "This category code is already assigned to another contact."
                    )

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.kannatusseura_cat_code}] {record.kannatusseura_cat_name}"
            result.append((record.id, name))
        return result
