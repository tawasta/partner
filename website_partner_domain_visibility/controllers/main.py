from odoo import http
from odoo.http import request
from odoo.tools.safe_eval import safe_eval


class WebsitePartnerDomain(http.Controller):
    @http.route("/website/partner_domain_check", type="json", auth="user")
    def check_partner_domain(self, filter_id):
        filter_rec = request.env["partner.domain.filter"].sudo().browse(filter_id)
        user_partner = request.env.user.partner_id

        if not filter_rec.exists() or not user_partner:
            return {"matched": False, "name": False}

        try:
            domain = safe_eval(filter_rec.filter_domain)
        except Exception:
            domain = []

        matched = (
            request.env["res.partner"]
            .sudo()
            .search_count([("id", "=", user_partner.id)] + domain)
            > 0
        )

        return {
            "matched": matched,
            "name": filter_rec.name,
        }
