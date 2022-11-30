from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        """Creates a partner with a Fiscal Position based on country_id"""
        partner = super(ResPartner, self).create(vals)

        european_union = self.sudo().env.ref("base.european_union").country_ids
        companies = self.env["res.company"].sudo().search([])
        country_id = vals.get("country_id")

        # Loop all companies
        for company in companies:
            # Company's partner's country is the domestic country
            domestic = company.partner_id.country_id.id

            domain = [("company_id", "=", company.id)]
            if (
                country_id
                and not partner.with_company(company.id).property_account_position_id
            ):

                # Check if a selected country is a domestic country
                if country_id == domestic:
                    domain += [("fiscal_type", "=", "domestic")]

                # Check if the selected country belong to European Union
                elif country_id in european_union.ids:
                    domain += [("fiscal_type", "=", "eu")]

                # Otherwise the selected country must reside outside EU
                else:
                    domain += [("fiscal_type", "=", "non_eu")]

                # Limit is one to avoid a possible error
                fiscal_position = (
                    self.env["account.fiscal.position"].sudo().search(domain, limit=1)
                )

                # Fiscal position is assigned within context of the looped company
                partner.with_company(
                    company.id
                ).property_account_position_id = fiscal_position
        return partner
