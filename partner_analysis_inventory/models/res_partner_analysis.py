from odoo import models


class ResPartnerAnalysis(models.Model):

    _inherit = "res.partner.analysis"

    def action_open_quants(self):
        # Show all quants
        self.ensure_one()

        action = self.env["ir.actions.act_window"].for_xml_id(
            "stock", "product_open_quants"
        )

        action.update(
            context=dict(self.env.context, search_default_locationgroup=True),
            domain=[("location_id", "in", self.location_ids.ids)],
        )

        return action
