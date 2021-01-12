import uuid
from odoo import _
from odoo import models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def pseudonymize(self):
        """
        Pseudonymize a partner
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
            "image": False,
        }
        # We leave city, zip and country be for reporting purposes
        # They aren't identifying information after other info is deleted
        for record in self:
            hash = str(uuid.uuid4())

            res_user = self.env["res.users"].sudo().search([
                ('partner_id', '=', record.id)
            ])
            if res_user:
                res_user.write({"active": False, "login": hash})

            if hasattr(record, "mass_mailing_contact_ids"):
                if record.mass_mailing_contact_ids:
                    for m in record.mass_mailing_contact_ids:
                        m.unlink()

            values["name"] = hash
            record.write(values)

            record.message_post(body=_("Partner pseudonymized"))
