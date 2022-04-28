# -*- coding: utf-8 -*-
from odoo import http

class HotelSandiara(http.Controller):
#	@http.route('/hotel_sandiara/hotel_sandiara/', auth='public')
#		return  http.request.render('hotel.index', {'teachers': ["Wélé", "Tall", "Ka"],})
#     @http.route('/hotel_sandiara/hotel_sandiara/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_sandiara.listing', {
#             'root': '/hotel_sandiara/hotel_sandiara',
#             'objects': http.request.env['hotel_sandiara.hotel_sandiara'].search([]),
#         })

#     @http.route('/hotel_sandiara/hotel_sandiara/objects/<model("hotel_sandiara.hotel_sandiara"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_sandiara.object', {
#             'object': obj
#         })



    @http.route('/hotel_sandiara/hotel_sandiara/', auth='public')
    def index(self, **kw):
        Location = http.request.env['hotel.location']
        return http.request.render('hotel.index', {
             'location': Location.search([])
         })
        

    # @http.route('/hotel/<model("hotel.location"):location>/', auth='public', website=True)
    # def location(self, location):
    #         return http.request.render('hotel.dateloc', {'person': location})