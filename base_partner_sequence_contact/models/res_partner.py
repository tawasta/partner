from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def _needs_ref(self, vals=None):
        res = super()._needs_ref(vals)
        # Always assign a reference
        res = True
        return res

    @api.model
    def _commercial_fields(self):
        """
        Make the partner reference a field that is propagated
        to the partner's contacts
        """
        res = super()._commercial_fields()

        return res
