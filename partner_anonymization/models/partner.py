import uuid
from datetime import datetime, timedelta

from odoo import _, fields, models
from odoo.tools.safe_eval import safe_eval


class ResPartner(models.Model):
    _inherit = "res.partner"

    date_to_be_anonymized = fields.Date(
        string="Anonymization schedule",
        help="Partner will be irreversibly anonymized on this date",
    )

    date_anonymized = fields.Datetime(
        "Anonymization date",
        readonly=True,
    )

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
            values["date_anonymized"] = fields.Datetime.now()
            record.write(values)

            record.message_post(body=_("Partner anonymized"))
            record.action_archive()

    def _cron_schedule_anonymize_partners(self):
        config = self.env["ir.config_parameter"].sudo()
        anonymize = config.get_param("partner_anonymization.anonymize")
        domain = config.get_param("partner_anonymization.domain")
        remove_delay = config.get_param("partner_anonymization.remove_delay")
        modification_delay = config.get_param(
            "partner_anonymization.modification_delay"
        )

        if not anonymize:
            # Auto-anonymization is not in use
            return

        modification = datetime.now() - timedelta(days=int(modification_delay))
        remove_date = fields.Date.today() + timedelta(days=int(remove_delay))

        domain = [
            ("write_date", "<=", modification),
            ("date_to_be_anonymized", "=", False),
        ] + safe_eval(domain)
        records = self.search(domain)
        records.write({"date_to_be_anonymized": remove_date})

    def _cron_anonymize_partners(self):
        config = self.env["ir.config_parameter"].sudo()
        anonymize = config.get_param("partner_anonymization.anonymize")

        if not anonymize:
            # Auto-anonymization is not in use
            return

        today = fields.Date.today()
        records = self.search([("date_to_be_anonymized", "<=", today)])

        records.anonymize()
