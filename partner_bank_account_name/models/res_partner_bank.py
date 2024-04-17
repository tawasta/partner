from odoo import api, fields, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    account_name = fields.Char("Account name", size=64)

    def name_get(self):
        result = super().name_get()
        new_result = []

        for res in result:
            acc = self.browse(res[0])
            if acc.account_name:
                name = "{} / {}".format(acc.account_name, res[1])
            else:
                name = res[1]

            if acc.company_id:
                name = "{} ({})".format(name, acc.company_id.name)

            new_result.append((acc.id, name))
        return new_result

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        args = args or []
        domain = []

        if name:
            domain = [
                "|",
                ("acc_number", "ilike", name),
                ("account_name", "ilike", name),
            ]

        accounts = self.search(domain + args, limit=limit)

        return accounts.name_get()
