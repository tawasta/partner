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

        values = self._get_anonymize_values()
        # We leave city, zip and country be for reporting purposes
        # They aren't identifying information after other info is deleted
        for record in self:
            user_hash = str(uuid.uuid4())
            res_user = (
                self.env["res.users"].sudo().search([("partner_id", "=", record.id)])
            )

            # Disable user
            if res_user:
                res_user.write({"active": False, "login": user_hash})

            values["name"] = user_hash
            values["date_anonymized"] = fields.Datetime.now()
            record.write(values)
            record.message_post(body=_("Partner anonymized"))

            # Anonymize mass mailing contacts, if they exist
            record.anonymize_mass_mailing_contact_ids()

            # Anonymize contracts, if they exist
            record.anonymize_contract_ids()

            # Anonymize subscriptions, if they exist
            record.anonymize_subscription_ids()

            # Anonymize tracking values
            record.anonymize_mail_messages()

            # Archive the anonymized partner
            record.action_archive()

    def _get_anonymize_values(self):
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

        return values

    def anonymize_mass_mailing_contact_ids(self):
        if not hasattr(self, "mass_mailing_contact_ids"):
            return

        # Unlink mass mailing contacts
        for record in self:
            if record.mass_mailing_contact_ids:
                for m in record.mass_mailing_contact_ids:
                    m.unlink()

    def anonymize_contract_ids(self):
        if not hasattr(self, "contract_ids"):
            return

        for record in self:
            contract_ids = (
                self.env["contract.contract"]
                .sudo()
                .search([("partner_id", "=", record.id)])
            )

            contract_ids.write({"name": record.name})

    def anonymize_subscription_ids(self):
        if not hasattr(self, "subscription_ids"):
            return

        for record in self:
            subscription_ids = (
                self.env["sale.subscription"]
                .sudo()
                .search([("partner_id", "=", record.id)])
            )

            for subscription in subscription_ids:
                # Recompute subscription names, if they include the partner name
                subscription.sale_subscription_line_ids._compute_name()

    def anonymize_mail_messages(self):
        # Anonymize mail messages and mail tracking values
        for record in self:
            for message in record.message_ids:
                message.tracking_value_ids.write(
                    {
                        "old_value_char": False,
                        "new_value_char": False,
                        "old_value_text": False,
                        "new_value_text": False,
                    }
                )

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
