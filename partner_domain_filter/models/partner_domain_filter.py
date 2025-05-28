from odoo import fields, models


class PartnerDomainFilter(models.Model):
    _name = "partner.domain.filter"
    _description = "Partner Domain Filter"

    name = fields.Char(string="Name", required=True)
    filter_domain = fields.Char(
        string="Filter Domain",
        required=True,
        help="Enter a domain expression in string format, "
        "e.g. [('country_id', '=', 'US')]",
    )
