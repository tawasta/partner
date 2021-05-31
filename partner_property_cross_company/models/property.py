from odoo import api
from odoo import models


class Property(models.Model):

    _inherit = "ir.property"

    @api.model
    def get_multi(self, name, model, ids):
        if model == "res.partner" and name in self._get_cross_company_fields():
            self = self.with_context(force_company=1)

        return super(Property, self).get_multi(name, model, ids)

    @api.model
    def set_multi(self, name, model, values, default_value=None):
        if model == "res.partner" and name in self._get_cross_company_fields():
            self = self.with_context(force_company=1)
        return super(Property, self).set_multi(name, model, values, default_value)

    def _get_cross_company_fields(self):
        fields = [
            "property_payment_term_id",
            "property_product_pricelist",
            "property_supplier_payment_term_id",
        ]

        return fields
