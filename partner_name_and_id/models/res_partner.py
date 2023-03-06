from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    def name_get(self):
        result = []
        for record in self:
            record_name = record.name + " - " + str(record.id)
            result.append((record.id, record_name))
        return result

    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []
        recs = self.search([("id", operator, name)] + args, limit=limit)
        if not recs.ids:
            return super(OpStudent, self).name_search(
                name=name, args=args, operator=operator, limit=limit
            )
        return recs.name_get()
