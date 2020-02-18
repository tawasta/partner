from odoo import fields, models


class AdditionalTerm(models.Model):

    _name = "res_partner_additional_terms.term"

    _description = "Additional Term"

    def _get_default_company(self):
        return self.env.user.company_id.id

    name = fields.Char(string="Name", required=True)

    contents = fields.Text(string="Term contents", required=True)

    company_id = fields.Many2one(
        comodel_name="res.company", string="Company", default=_get_default_company
    )
