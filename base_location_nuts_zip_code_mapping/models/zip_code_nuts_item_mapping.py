from odoo import fields, models


class ZipCodeNUTSItemMapping(models.Model):
    _name = "res.zip_code_nuts_item_mapping"
    _description = "Zip Code NUTS Item Mapping"

    country_id = fields.Many2one(
        comodel_name="res.country", string="Country", required=True
    )

    zip_code = fields.Char(required=True)
    region_name = fields.Char()
    municipality_name = fields.Char()
    municipality_code = fields.Char()

    imported_from_posti_pcf_file = fields.Boolean(
        string="Imported from Posti's PCF file",
        default=False,
        help="Whether this mapping was created as a result of a importing "
        "from a Posti PCF .dat file",
    )

    nuts_item_id = fields.Many2one(
        comodel_name="res.partner.nuts",
        string="Matching NUTS Item",
        required=True,
        domain=[("level", "=", 4)],
    )
