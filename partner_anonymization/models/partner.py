import uuid

from odoo import _, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def _get_chatter_messages_domain(self):
        self.ensure_one()
        return [
            "|",
            "|",
            "&",
            ("model", "=", "res.partner"),
            ("res_id", "=", self.id),
            ("author_id", "=", self.id),
            ("partner_ids", "in", [self.id]),
        ]

    def _delete_chatter_messages(self):
        self.ensure_one()
        messages = self.env["mail.message"].sudo().search(
            self._get_chatter_messages_domain()
        )
        if messages:
            messages.unlink()

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
                    if record.name in contract.name:
                        splitted_name = contract.name.split(record.name)[1]
                        new_name = user_hash + splitted_name
                    else:
                        new_name = user_hash
                    contract.write({"name": new_name})

            if hasattr(record, "mass_mailing_contact_ids"):
                if record.mass_mailing_contact_ids:
                    for m in record.mass_mailing_contact_ids:
                        m.unlink()

            values["name"] = user_hash
            record.write(values)

            record._delete_chatter_messages()
            record.message_post(body=_("Partner anonymized"))
            record.action_archive()