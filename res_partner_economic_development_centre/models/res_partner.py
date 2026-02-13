import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    economic_development_centre_id = fields.Many2one(
        comodel_name="economic.development.centre", string="Economic Development Centre"
    )

    @api.onchange("zip", "country_id")
    def _on_change_zip_country_edc(self):
        # Looks up a matching economic development centre based
        # on the zip code to municipality code info provided by posti, and
        # municipality code to EDC code provided by stat.fi
        #
        # This lookup chain is a bit convoluted due to the EDC to municipality code
        # mapping table consisting simply of dumb code pairs extracted from stat.fi
        # material.

        zip_nuts_mapping_obj = self.env["res.zip_code_nuts_item_mapping"]
        municipality_code_edc_code_mapping_obj = self.env[
            "res.municipalicy_code_edc_code_mapping"
        ]
        economic_development_centre_obj = self.env["economic.development.centre"]

        for record in self:
            if not record.country_id or not record.zip:
                continue

            zip_sanitized = record.zip.strip()

            # Look for a mapping between partner's zip code and municipality code
            matching_zip_nuts_mapping = zip_nuts_mapping_obj.sudo().search(
                domain=[
                    ("country_id", "=", record.country_id.id),
                    ("zip_code", "=", zip_sanitized),
                ],
                limit=1,
            )

            if matching_zip_nuts_mapping:
                # Look for a mapping the municipality code and EDC code
                matching_edc_mapping = municipality_code_edc_code_mapping_obj.search(
                    domain=[
                        (
                            "municipality_code",
                            "=",
                            matching_zip_nuts_mapping.municipality_code,
                        )
                    ],
                    limit=1,
                )

                if matching_edc_mapping:
                    # Finally look for the actual EDC based on its code
                    matching_edc = economic_development_centre_obj.search(
                        domain=[
                            (
                                "code",
                                "=",
                                matching_edc_mapping.economic_development_centre_code,
                            )
                        ]
                    )

                    if matching_edc:
                        record.economic_development_centre_id = matching_edc.id
