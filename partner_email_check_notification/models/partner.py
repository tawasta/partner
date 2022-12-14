import logging

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):

    _inherit = "res.partner"

    email_invalid = fields.Char("Invalid email", readonly=True)

    @api.constrains("email")
    def _check_email_unique(self):
        res = False
        try:
            res = super()._check_email_unique()
        except UserError as e:
            self.email_invalid = e

        return res

    def _normalize_email(self, email):
        try:
            res = super()._normalize_email(email)
            self.email_invalid = False
        except ValidationError as e:
            self.email_invalid = e
            res = email

        return res
