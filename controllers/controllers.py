# -*- coding: utf-8 -*-
from odoo import http


# class Costing(http.Controller):
#     @http.route('/costing/costing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/costing/costing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('costing.listing', {
#             'root': '/costing/costing',
#             'objects': http.request.env['costing.costing'].search([]),
#         })

#     @http.route('/costing/costing/objects/<model("costing.costing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('costing.object', {
#             'object': obj
#         })
