from odoo import http
from odoo.http import request


class HotelWebsite(http.Controller):
    @http.route('/hotel', website=True, auth='public')
    def hotel(self):
        users_deatils = request.env['res.partner'].sudo().search([])

        return request.render('hotel_management.hotel_page', {
            'customer': users_deatils,
        })
