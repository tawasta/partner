from odoo import fields, models


class ResPartnerDateRange(models.Model):
    _name = "res.partner.date.range"
    _description = "Partner Date Range Information"
    _rec_name = "display_name"

    partner_id = fields.Many2one(
        "res.partner", string="Partner", required=True, ondelete="cascade"
    )

    type_id = fields.Many2one(
        "res.partner.date.range.type",
        string="Type",
        required=True,
        ondelete="restrict",
    )

    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")
    notes = fields.Text(string="Internal Notes")
