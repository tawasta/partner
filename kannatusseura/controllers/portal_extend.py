from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class PortalExtend(CustomerPortal):

    def _get_optional_fields(self):
        fields = super()._get_optional_fields()
        fields.append('kannatusseura_id')
        return fields

    def details_form_validate(self, data):
        error, error_message = super().details_form_validate(data)
        return error, error_message

    def details_form_save(self, values):
        partner = request.env.user.partner_id.sudo()
        kannatusseura_id = values.pop('kannatusseura_id', False)
        if kannatusseura_id:
            partner.write({'kannatusseura_id': int(kannatusseura_id)})
        return super().details_form_save(values)

    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        response = super().account(redirect=redirect, **post)
        qcontext = response.qcontext

        kannatusseurat = request.env['kannatusseura.kannatusseura'].sudo().search([], order="name ASC")
        qcontext.update({
            'kannatusseurat': kannatusseurat,
            'selected_kannatusseura_id': request.env.user.partner_id.kannatusseura_id.id or False,
        })
        return response
