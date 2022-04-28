# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderVikafandila(http.Controller):
#     @http.route('/booking_order_Vikafandila/booking_order_Vikafandila/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_Vikafandila/booking_order_Vikafandila/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_Vikafandila.listing', {
#             'root': '/booking_order_Vikafandila/booking_order_fitra',
#             'objects': http.request.env['booking_order_Vikafandila.booking_order_Vikafandila'].search([]),
#         })

#     @http.route('/booking_order_Vikafandila/booking_order_Vikafandila/objects/<model("booking_order_Vikafandila.booking_order_Vikafandila"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_Vikafandila.object', {
#             'object': obj
#         })
