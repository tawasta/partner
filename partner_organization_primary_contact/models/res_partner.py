from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_primary_contact = fields.Boolean(
        string="Primary Contact",
        help="Whether the contact is considered the primary contact of their "
        "organization",
        tracking=True,
    )
