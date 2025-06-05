from odoo import fields, models


class PartnerDomainFilter(models.Model):
    _name = "partner.domain.filter"
    _description = "Partner Domain Filter"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer()
    description = fields.Text()
    filter_domain = fields.Char(
        string="Filter Domain",
        required=True,
        help="Enter a domain expression in string format, "
        "e.g. [('country_id', '=', 'US')]",
    )
