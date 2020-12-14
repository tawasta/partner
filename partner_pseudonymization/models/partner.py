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
        }
        # We leave city, zip and country be for reporting purposes
        # They aren't identifying information after other info is deleted
        for record in self:
            values["name"] = uuid.uuid4()
            record.write(values)

            record.message_post(body=_("Partner pseudonymized"))
