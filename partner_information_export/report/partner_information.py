from collections import OrderedDict

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
            columns = self._get_data_to_export(o)

            self._add_sheet(o._description, workbook, columns)

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
                    columns = self._get_data_to_export(records)

                    if columns:
                        self._add_sheet(
                            model._description or model._name, workbook, columns
                        )

            o.message_post(body=_("Partner information exported"))

    def _get_data_to_export(self, records):
        """
        Get headers and rows to write in the XLXS-file
        """
        columns = OrderedDict()
        for record in records:
            for field in record._fields:
                odoo_field = record._fields[field]
                if (
                    not odoo_field.groups
                    or odoo_field.groups in self.env.user.groups_id
                ):
                    key = field.split(":", maxsplit=1)[0]
                    if key[0] == "_":
                        # Skip private attributes
                        continue
                    value = getattr(record, key)
                    if not isinstance(value, float | int | bool | str):
                        # Skip relation fields for now
                        # They arguably could be included, but needs testing
                        continue

                    if key.startswith("message_") or key.startswith("user_"):
                        # Skip exporting message and user fields
                        continue

                    if key not in columns:
                        columns[key] = []

                    columns[key].append(value)

        return columns

    def _add_sheet(self, sheet_name, workbook, columns):
        """
        Add a new sheet, headers and rows
        """
        sheet = workbook.add_worksheet(sheet_name)

        sheet.set_row(0, None, None, {"collapsed": 1})
        bold = workbook.add_format({"bold": True})

        # Write columns
        c = 0
        for header, values in columns.items():
            if not all(values):
                # Skip columns without values
                continue

            # Add header
            sheet.write(0, c, header, bold)
            # Start values from second row
            r = 1
            for value in values:
                sheet.write(r, c, value)
                r += 1

            # Next value, next column
            c += 1
