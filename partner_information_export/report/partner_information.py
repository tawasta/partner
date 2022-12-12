from odoo import _, models


class PartnerInformationXlsx(models.AbstractModel):
    _name = "report.partner_information_export.partner_information_xlsx"
    _description = "Partner information XLSX Report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, objects):
        """
        Export all partner information
        """

        for o in objects:
            # Export partner basic information
            headers, rows = self._get_data_to_export(o)

            self._add_sheet(o._description, workbook, headers, rows)

            # Export related records
            partner_model = (
                self.env["ir.model"].sudo().search([("model", "=", "res.partner")])
            )
            for field in partner_model.field_id:
                # TODO: Support many2many records
                # TODO: Support related "rows", e.g. sale order lines, invoice lines
                if field.ttype == "one2many" and field.store is True:
                    model = self.env[field.relation]

                    if model._name.startswith("mail"):
                        # Skip mail-relations
                        continue

                    records = model.search([(field.relation_field, "=", o.id)])
                    headers, rows = self._get_data_to_export(records)

                    if rows:
                        self._add_sheet(
                            model._description or model._name, workbook, headers, rows
                        )

            o.message_post(body=_("Partner information exported"))

    def _get_data_to_export(self, records):
        """
        Get headers and rows to write in the XLXS-file
        """
        headers = []
        rows = []
        first = True
        for record in records:
            values = []
            for field in record._fields:
                key = field.split(":", maxsplit=1)[0]
                if key[0] == "_":
                    # Skip private attributes
                    continue
                value = getattr(record, key)
                if not isinstance(value, (float, int, bool, str)):
                    # Skip relation fields for now
                    # They arguably could be included, but needs testing
                    continue

                if key.startswith("message"):
                    # Skip exporting message fields
                    continue

                if first:
                    headers.append(key)

                values.append(str(value))

            first = False
            rows.append(values)

        return headers, rows

    def _add_sheet(self, sheet_name, workbook, headers, rows):
        """
        Add a new sheet, headers and rows
        """
        sheet = workbook.add_worksheet(sheet_name)

        sheet.set_row(0, None, None, {"collapsed": 1})
        sheet.write_row(0, 0, headers)

        i = 1
        for row in rows:
            col = 0
            for column in row:
                sheet.write(i, col, column)
                col += 1
