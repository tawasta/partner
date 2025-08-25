import logging

from odoo import http
from odoo.http import request
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class WebsitePartnerDomain(http.Controller):
    @http.route("/website/partner_domain_check", type="json", auth="user")
    def check_partner_domain(self, filter_id):
        filter_rec = request.env["partner.domain.filter"].sudo().browse(filter_id)
        user_partner = request.env.user.partner_id

        if not filter_rec.exists() or not user_partner:
            _logger.info(
                "PartnerDomainCheck: Filter ei löytynyt tai ei partneria. filter_id=%s",
                filter_id,
            )
            return {"matched": False, "name": False}

        try:
            domain = safe_eval(filter_rec.filter_domain)
        except Exception:
            _logger.warning("PartnerDomainCheck: filter_domain eval epäonnistui")
            domain = []

        matched = (
            request.env["res.partner"]
            .sudo()
            .search_count([("id", "=", user_partner.id)] + domain)
            > 0
        )

        _logger.info(
            "PartnerDomainCheck: Käyttäjä %s, filter '%s' (%s), matched=%s, domain=%s",
            user_partner.id,
            filter_rec.name,
            filter_rec.id,
            matched,
            domain,
        )

        return {
            "matched": matched,
            "name": filter_rec.name,
        }
