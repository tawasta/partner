import urllib.parse

import requests

from odoo import _, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def action_update_info_from_prh(self):
        for record in self:
            api_url = "https://avoindata.prh.fi/opendata-ytj-api/v3/companies?"
            params = self._get_prh_search_params()

            if params:
                search_url = f"{api_url}{urllib.parse.urlencode(params)}"
            else:
                title = _("No search terms")
                message = _("Please set name, company registry or VAT")
                return {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "title": title,
                        "message": message,
                        "sticky": False,
                    },
                }

            response = requests.get(search_url).json()
            count = len(response.get("companies"))

            if count == 0:
                title = _("No results")
                message = _("Could not find any results")
            elif count > 1:
                title = _("Multiple results")
                message = _("Found multiple results. Please be more specific")
            else:
                values = record._parse_prh_response(response.get("companies"))

                # TODO: The line break doesn't actually work. <br/> won't work either.
                update_string = ",\n".join(
                    [value for key, value in values.items() if isinstance(value, str)]
                )
                title = _("Company info updated!")
                message = _(f"{update_string}")

            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": title,
                    "message": message,
                    "sticky": True,
                    "next": {
                        "type": "ir.actions.act_window_close",
                    },
                },
            }

    def _get_prh_search_params(self):
        self.ensure_one()
        params = {}
        if self.name:
            # Search by name
            params["name"] = self.name

        company_registry = self.company_registry
        vat = self.vat

        if not company_registry and vat and vat[0:2] == "FI":
            # Construct company registry from Finnish VAT code
            company_registry = f"{vat[2:-1]}-{vat[-1]}"

        if company_registry:
            params["businessId"] = company_registry

        return params

    def _parse_prh_response(self, companies):
        self.ensure_one()
        values = {}
        company = companies[0]

        if company.get("names"):
            # Update name
            values["name"] = company.get("names")[0].get("name")

        if company.get("businessId"):
            values["company_registry"] = company.get("businessId").get("value")

        if company.get("website"):
            values["website"] = company["website"].get("url")

        # Update address details
        if company.get("addresses"):
            # TODO: this can only handle the first address.
            #  We could create affiliate companies from other addresses

            address = company["addresses"][0]
            street = []

            if address.get("street"):
                street.append(address["street"])
            if address.get("postCode"):
                values["zip"] = address["postCode"]
            if address.get("postOffices"):
                values["city"] = address["postOffices"][0].get("city")
            if address.get("buildingNumber"):
                street.append(address["buildingNumber"])
            if address.get("entrance"):
                street.append(address["entrance"])
            if address.get("apartmentNumber"):
                street.append(address["apartmentNumber"])
            if address.get("apartmentIdSuffix"):
                street.append(address["apartmentIdSuffix"])
            if address.get("co"):
                street.append(address["co"])

            if street:
                # Construct the street
                values["street"] = " ".join(street)

            # TODO: make configurable
            use_industry = True

            business_line = company.get("mainBusinessLine")
            if use_industry and business_line:
                values["industry_id"] = self._get_or_create_industry(business_line).id

        self.write(values)

        return values

    def _get_or_create_industry(self, business_line):
        # Get or create an industry

        # TODO: configurable code
        # 1: finnish
        # 2: swedish
        # 3: english
        language_code = str(1)
        name = ""

        for desc in business_line.get("descriptions"):
            if desc.get("languageCode") == language_code:
                name = desc.get("description")

        code = business_line.get("type")

        industry_model = self.env["res.partner.industry"].sudo()

        industry = industry_model.search(
            ["|", ("name", "=ilike", name), ("full_name", "ilike", code)], limit=1
        )

        if not industry:
            industry = industry_model.create(
                {
                    "name": name,
                    "full_name": f"[{code}] {name}",
                }
            )

        return industry
