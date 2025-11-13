# -*- coding: utf-8 -*-
# from odoo import http


# class Kannatusseura(http.Controller):
#     @http.route('/kannatusseura/kannatusseura', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kannatusseura/kannatusseura/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kannatusseura.listing', {
#             'root': '/kannatusseura/kannatusseura',
#             'objects': http.request.env['kannatusseura.kannatusseura'].search([]),
#         })

#     @http.route('/kannatusseura/kannatusseura/objects/<model("kannatusseura.kannatusseura"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kannatusseura.object', {
#             'object': obj
#         })

