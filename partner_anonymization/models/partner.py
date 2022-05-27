import uuid

from odoo import _, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def anonymize(self):
        """
        Anonymize a partner
        :return:
        """

        values = {
            "street": False,
            "street2": False,
            "active": False,
            "email": False,
            "title": False,
            "phone": False,
            "mobile": False,
            "website": False,
        }
        # We leave city, zip and country be for reporting purposes
        # They aren't identifying information after other info is deleted
        for record in self:
            user_hash = str(uuid.uuid4())
            res_user = (
                self.env["res.users"].sudo().search([("partner_id", "=", record.id)])
            )
            contract_ids = (
                self.env["contract.contract"]
                .sudo()
                .search([("partner_id", "=", record.id)])
            )

            if res_user:
                res_user.write({"active": False, "login": user_hash})

            if contract_ids:
                for contract in contract_ids:
                    splitted_name = contract.name.split(record.name)[1]
                    new_name = user_hash + splitted_name
                    contract.write({"name": new_name})

            if hasattr(record, "mass_mailing_contact_ids"):
                if record.mass_mailing_contact_ids:
                    for m in record.mass_mailing_contact_ids:
                        m.unlink()

            values["name"] = user_hash
            record.write(values)

            record.message_post(body=_("Partner anonymized"))
