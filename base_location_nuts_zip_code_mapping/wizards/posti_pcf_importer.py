import base64
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PostiImportWizard(models.TransientModel):
    _name = "posti.pcf.importer.wizard"
    _description = "Import Posti PCF from uploaded file"

    file_data = fields.Binary(string="PCF File (.dat)", required=True, attachment=True)
    file_name = fields.Char()

    clear_existing_mappings = fields.Boolean(
        default=True,
        help="Deletes existing mappings imported from Posti materials. Keeps any "
        "manually created ones.",
    )

    recompute_partner_nuts_items = fields.Boolean(
        string="Recompute Partners' NUTS Levels",
        default=True,
        help="Triggers the recomputation of existing partners NUTS levels based on "
        "their current ZIP codes and countries",
    )

    # fixed positions in the DAT file
    ZIP = (13, 18)
    REGION_NAME = (116, 146)
    MUNICIPALITY_CODE = (175, 179)
    MUNICIPALITY_NAME = (179, 198)

    def _slice(self, line, span):
        # Extract a part of a line
        return line[span[0] : span[1]].strip()

    def _find_nuts_l4_item(self, region_name):
        # Find a name-based match from the NUTS L4 data in Odoo for e.g.
        # 'Pirkanmaa'

        res_partner_nuts_obj = self.env["res.partner.nuts"]

        # Ahvenanmaa needs to be handled separately, NUTS uses its swedish name
        # but posti data uses its finnish name
        if region_name == "Ahvenanmaa":
            matching_nuts_item = res_partner_nuts_obj.search(
                domain=[("level", "=", 4), ("name", "=", "Åland")], limit=1
            )
        else:
            matching_nuts_item = res_partner_nuts_obj.search(
                domain=[("level", "=", 4), ("name", "=", region_name)], limit=1
            )

        if not matching_nuts_item:
            # return the extra region placeholder if no matches
            matching_nuts_item = res_partner_nuts_obj.search(
                domain=[("code", "=", "FIZZZ")], limit=1
            )

        return matching_nuts_item

    def _parse_line(self, line):
        # Extract the relevant data from the line
        if len(line) < 198 or not line.startswith("PONOT"):
            return None

        zip_code = self._slice(line, self.ZIP)
        municipality_code = self._slice(line, self.MUNICIPALITY_CODE)
        municipality_name = self._slice(line, self.MUNICIPALITY_NAME)
        region_name = self._slice(line, self.REGION_NAME)

        return (zip_code, municipality_code, municipality_name, region_name)

    def action_parse_posti_pcf_file(self):
        # Parse the uploaded DAT file from https://www.posti.fi/webpcode
        # and store mappings

        self.ensure_one()

        mapping_obj = self.env["res.zip_code_nuts_item_mapping"]

        if self.clear_existing_mappings:
            mapping_obj.search(
                [("imported_from_posti_pcf_file", "=", True)]
            ).sudo().unlink()

        decoded_file = base64.b64decode(self.file_data)
        rows = []

        for raw_line in decoded_file.splitlines():
            if not raw_line:
                continue

            line = raw_line.decode("latin-1")
            parsed = self._parse_line(line)
            if parsed:
                rows.append(parsed)

        if not rows:
            return

        for zip_code, municipality_code, municipality_name, region_name in rows:
            matching_nuts_item_id = self._find_nuts_l4_item(region_name)

            mapping_obj.create(
                {
                    "country_id": self.env.ref("base.fi").id,
                    "zip_code": zip_code,
                    "region_name": region_name,
                    "municipality_name": municipality_name,
                    "municipality_code": municipality_code,
                    "nuts_item_id": matching_nuts_item_id.id,
                    "imported_from_posti_pcf_file": True,
                }
            )

        if self.recompute_partner_nuts_items:
            all_partners = self.env["res.partner"].sudo().search([])
            all_partners._on_change_zip_country()

        return {"type": "ir.actions.act_window_close"}
