from odoo import models
from odoo import fields


class ResPartner(models.Model):

    _inherit = "res.partner"

    property_payment_term_id = fields.Many2one(
        "account.payment.term", company_dependent=False
    )
