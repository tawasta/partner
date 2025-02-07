from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    full_name = fields.Char(
        string="Full name", compute="_compute_full_name", index=True, store=True
    )

    @api.depends("name", "parent_id")
    def _compute_full_name(self):
        for record in self:
            name = self._get_recursive_name(record)
            record.full_name = name

    def _get_recursive_name(self, record):
        """Returns a recursive partner name"""
        if record.parent_id:
            name = f"{self._get_recursive_name(record.parent_id)}, {record.name}"
        else:
            name = record.name

        return name
