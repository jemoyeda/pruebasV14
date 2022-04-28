# -*- coding: utf-8 -*-
# from odoo import http


# class AngelBookingOrder(http.Controller):
#     @http.route('/angel_booking_order/angel_booking_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/angel_booking_order/angel_booking_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('angel_booking_order.listing', {
#             'root': '/angel_booking_order/angel_booking_order',
#             'objects': http.request.env['angel_booking_order.angel_booking_order'].search([]),
#         })

#     @http.route('/angel_booking_order/angel_booking_order/objects/<model("angel_booking_order.angel_booking_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('angel_booking_order.object', {
#             'object': obj
#         })
