import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    email_secondary = fields.Char(
        string="Email (Secondary)", help="Contact's secondary e-mail address."
    )
