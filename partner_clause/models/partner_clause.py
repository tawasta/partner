from odoo import fields, models


class PartnerClause(models.Model):

    _name = "partner.clause"

    name = fields.Char(string="Name")
    clause = fields.Text(string="Clause", help="This is added to text-field.")
    used_for = fields.Selection(
        [("sale", "Sale"), ("invoice", "Invoice")],
        string="User for",
        default=False,
        copy=False,
        help=("Select where this clause is being used."),
    )
