from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    alias_ids = fields.One2many(
        "res.partner.alias",
        "partner_id",
        string="Alternative Names",
        help="Alternative customer names",
    )

    @property
    def _rec_names_search(self):
        return super()._rec_names_search + ["alias_ids.name"]

    def _find_or_create_aliases(self, names):
        self.ensure_one()
        existing_names = {alias.name.lower() for alias in self.alias_ids}
        to_create = []
        for name in names:
            name = (name or "").strip()
            if not name:
                continue
            if name.lower() in existing_names:
                continue
            existing_names.add(name.lower())
            to_create.append({"name": name, "partner_id": self.id})
        return self.env["res.partner.alias"].create(to_create)
