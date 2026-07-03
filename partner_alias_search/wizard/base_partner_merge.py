from odoo import models


class BasePartnerMergeAutomaticWizard(models.TransientModel):
    _inherit = "base.partner.merge.automatic.wizard"

    def _merge(self, partner_ids, dst_partner=None, extra_checks=True):
        partners = self.env["res.partner"].browse(partner_ids).exists()

        target_partner = dst_partner
        alias_names = (partners - target_partner).mapped("name")

        result = super()._merge(
            partner_ids,
            dst_partner=dst_partner,
            extra_checks=extra_checks,
        )

        if target_partner.exists():
            target_partner._find_or_create_aliases(alias_names)

        return result