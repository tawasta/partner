from odoo import http
from odoo.http import request

class CustomerPortalDetails(http.Controller):
    
    #Prefetch the values for dropdown
    def _prepare_portal_layout_values(self):
        values = {}
        values['kannatusseurat'] = request.env['kannatusseura.model'].sudo().search([])
        return values 

    #Populate the field
    @http.route(['/my/account'], type='http', auth='user', website=True)
    def portal_my_details(self, **kwargs):
        partner = request.env.user.partner_id
        kannatusseurat = request.env['kannatusseura.model'].sudo().search([])
        values = {
            'partner': partner,
            'kannatusseurat': kannatusseurat,
            'error': {},
        }
        return request.render('portal.portal_my_details', values)

    #Save changes; update form, handle errors and update db and backend.
    #   Overrides part of the default functionality of the portal save button.
    @http.route(['/my/account/save'], type='http', auth='user', website=True, methods=['POST'])
    def portal_my_details_save(self, **kwargs): 
        partner = request.env.user.partner_id
        error = {}

        kannatusseura_id = kwargs.get('user_kannatusseura')
        if kannatusseura_id:
            try:
                kannatusseura_id = int(kannatusseura_id)
                if not request.env['kannatusseura.model'].sudo().browse(kannatusseura_id).exists():
                    error['kannatusseura'] = "Invalid selection"
            except ValueError:
                error['kannatusseura'] = "Invalid value"

        if not error:
            partner.sudo().write({
                'user_kannatusseura': kannatusseura_id or False,
                'email': kwargs.get('email'),
                'name': kwargs.get('name'),
            })
            return request.redirect('/my/account')

        kannatusseurat = request.env['kannatusseura.model'].sudo().search([])
        values = {
            'partner': partner,
            'kannatusseurat': kannatusseurat,
            'error': error,
        }
        return request.render('portal.portal_my_details', values)