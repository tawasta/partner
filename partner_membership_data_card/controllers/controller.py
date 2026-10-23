from odoo import http
from odoo.http import request


class MembershipPortal(http.Controller):
    @http.route("/my/membership-card", type="http", auth="user", website=True)
    def membership_card(self, **kwargs):
        partner = request.env.user.partner_id

        pdf_content, _ = (
            request.env["ir.actions.report"]
            .sudo()
            ._render_qweb_pdf(
                "partner_membership_data_card.partner_card_template", partner.ids
            )
        )

        return request.make_response(
            pdf_content,
            headers=[
                ("Content-Type", "application/pdf"),
                (
                    "Content-Disposition",
                    f'attachment; filename="membership_card_{partner.id}.pdf"',
                ),
            ],
        )
