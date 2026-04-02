from odoo import models


class ReportPartnerCertificate(models.AbstractModel):
    _name = "partner_member_certificate_report.member_certificate"
    _description = "Partner Member Certificate Report"

    def _get_report_values(self, docids, data=None):
        docs = self.env["res.partner"].browse(docids)
        return {
            "docs": docs,
            "env": self.env,
        }
