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
        # Make ref a not commercial field
        res = super()._commercial_fields()

        res.remove("ref")

        return res
