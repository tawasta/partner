from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange("street")
    def _onchange_street(self):
        self.geo_localize()

    @api.onchange("street2")
    def _onchange_street2(self):
        self.geo_localize()

    @api.onchange("city")
    def _onchange_city(self):
        self.geo_localize()

    @api.onchange("state_id")
    def _onchange_state_id(self):
        self.geo_localize()

    @api.onchange("zip")
    def _onchange_zip(self):
        self.geo_localize()

    @api.onchange("country_id")
    def _onchange_country_id(self):
        self.geo_localize()

    def geo_localize_next_empty(self):
        for partner in self.env["res.partner"].search([]):
            if partner.partner_latitude == 0.0 and partner.partner_longitude == 0.0:
                partner.geo_localize()
                break
