from odoo import fields, models


class ResPartnerAlias(models.Model):
    _name = "res.partner.alias"
    _description = "Contact Alternative Name"
    _order = "name, id"
    _rec_name = "name"

    name = fields.Char(required=True,)

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        ondelete="cascade",
        index=True,
    )

    active = fields.Boolean(default=True)