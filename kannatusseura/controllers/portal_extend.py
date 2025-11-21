from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class PortalExtend(CustomerPortal):

    def _get_optional_fields(self):
        fields = super()._get_optional_fields()
        fields.append('kannatusseura_id')
        return fields

    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        if post:
            error, error_message = self.details_form_validate(post)
            if not error:
                partner_fields = list(request.env['res.partner']._fields.keys())
                values = {}
                
                for key in self.MANDATORY_BILLING_FIELDS:
                    if key in post and key in partner_fields:
                        values[key] = post.get(key)
                
                for key in self.OPTIONAL_BILLING_FIELDS:
                    if key in post and key in partner_fields:
                        values[key] = post.get(key)
                
                if 'kannatusseura_id' in post:
                    try:
                        values['kannatusseura_id'] = int(post['kannatusseura_id']) if post['kannatusseura_id'] else False
                    except (ValueError, TypeError):
                        values['kannatusseura_id'] = False
                
                if values:
                    request.env.user.partner_id.sudo().write(values)
                
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')
        
        response = super().account(redirect=redirect, **post)
        qcontext = response.qcontext
        
        kannatusseurat = request.env['kannatusseura.kannatusseura'].sudo().search([], order="name ASC")
        qcontext.update({
            "kannatusseurat": kannatusseurat,
            "selected_kannatusseura_id": request.env.user.partner_id.kannatusseura_id.id,
        })
        
        return response