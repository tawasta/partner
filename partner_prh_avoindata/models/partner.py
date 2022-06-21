import requests

from odoo import models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def action_update_info_from_prh(self):
        for record in self:
            if record.business_code:
                url = "http://avoindata.prh.fi/tr/v1/" + record.business_code
            else:
                continue

            response = requests.get(url)
            json_response = response.json()

            if "results" not in json_response:
                return False

            if len(json_response["results"]) == 0:
                return False

            results = json_response["results"][0]

            # Update name
            if results.get("name"):
                record.name = results["name"]

            # Update address details
            if "addresses" in results:
                # TODO: this can only handle the first address.
                # Create affiliate companies from other addresses

                address = results["addresses"][0]

                if address.get("website"):
                    record.website = address["website"]
                if address.get("city"):
                    record.city = address["city"]
                if address.get("country"):
                    record.country_id = (
                        record.env["res.country"]
                        .search([("code", "=", address["country"])], limit=1)
                        .id
                    )
                if address.get("phone"):
                    record.phone = address["phone"]
                if address.get("street"):
                    record.street = address["street"]
                if address.get("postCode"):
                    record.zip = address["postCode"]
