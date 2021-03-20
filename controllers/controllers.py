# -*- coding: utf-8 -*-
# from odoo import http


# class Openhospital(http.Controller):
#     @http.route('/openhospital/openhospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openhospital/openhospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openhospital.listing', {
#             'root': '/openhospital/openhospital',
#             'objects': http.request.env['openhospital.openhospital'].search([]),
#         })

#     @http.route('/openhospital/openhospital/objects/<model("openhospital.openhospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openhospital.object', {
#             'object': obj
#         })
