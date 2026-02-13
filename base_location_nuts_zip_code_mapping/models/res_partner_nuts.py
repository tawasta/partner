from odoo import fields, models


class ResPartnerNuts(models.Model):
    _inherit = "res.partner.nuts"

    zip_code_nuts_item_mapping_ids = fields.One2many(
        comodel_name="res.zip_code_nuts_item_mapping",
        inverse_name="nuts_item_id",
        string="Zip Code NUTS Item Mappings",
    )
