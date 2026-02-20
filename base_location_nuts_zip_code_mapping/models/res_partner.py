import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange("zip", "country_id")
    def _on_change_zip_country(self):
        # Try to find a matching Country+ZIP <--> NUTS L4 mapping.
        # If found, auto-populate the partner's NUTS L1-L4 fields

        _logger.info("edc NUTS reached")

        zip_nuts_mapping_obj = self.env["res.zip_code_nuts_item_mapping"]

        for record in self:
            if not record.country_id or not record.zip:
                continue

            zip_sanitized = record.zip.strip()

            matching_zip_nuts_mapping = zip_nuts_mapping_obj.sudo().search(
                domain=[
                    ("country_id", "=", record.country_id.id),
                    ("zip_code", "=", zip_sanitized),
                ],
                limit=1,
            )

            if matching_zip_nuts_mapping:
                record.nuts4_id = matching_zip_nuts_mapping.nuts_item_id.id
                record.nuts3_id = matching_zip_nuts_mapping.nuts_item_id.parent_id.id
                record.nuts2_id = (
                    matching_zip_nuts_mapping.nuts_item_id.parent_id.parent_id.id
                )
                record.nuts1_id = (
                    matching_zip_nuts_mapping.nuts_item_id.parent_id.parent_id.parent_id.id  # noqa: E501
                )
