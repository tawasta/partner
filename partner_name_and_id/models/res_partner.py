from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def name_get(self):
        result = []
        for record in self:
            record_name = record.name + " - " + str(record.id)
            result.append((record.id, record_name))
        return result
