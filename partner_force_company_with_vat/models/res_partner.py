from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        if "vat" in vals:
            vals["is_company"] = True
            vals["company_type"] = "company"

        return super().create(vals)

    def write(self, vals):
        if "vat" in vals:
            vals["is_company"] = True
            vals["company_type"] = "company"

        return super().write(vals)
