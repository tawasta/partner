# -*- coding: utf-8 -*-
from odoo import fields, models


class IrFilters(models.Model):
    _inherit = "ir.filters"

    auto_rule_id = fields.Many2one(
        "role.irfilter.rule",
        string="Auto rule",
        index=True,
        ondelete="set null",
        help="If set, this filter is managed automatically by Role Auto IR Filters.",
    )
