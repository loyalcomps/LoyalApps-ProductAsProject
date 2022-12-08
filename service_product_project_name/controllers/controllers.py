# -*- coding: utf-8 -*-
# from odoo import http


# class ServiceProductProjectName(http.Controller):
#     @http.route('/service_product_project_name/service_product_project_name', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/service_product_project_name/service_product_project_name/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('service_product_project_name.listing', {
#             'root': '/service_product_project_name/service_product_project_name',
#             'objects': http.request.env['service_product_project_name.service_product_project_name'].search([]),
#         })

#     @http.route('/service_product_project_name/service_product_project_name/objects/<model("service_product_project_name.service_product_project_name"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('service_product_project_name.object', {
#             'object': obj
#         })
