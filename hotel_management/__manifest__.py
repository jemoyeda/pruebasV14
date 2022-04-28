# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hotel Management',
    'version' : '1.1',
    'summary': 'Hotel Management Software',
    'sequence': 10,
    'description': """Hotel Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['base','stock','account','mail','product','website'],
    'data': [
        'security/hotel_users_access_rights.xml',
        'security/ir.model.access.csv',
        'data/accommodation_series.xml',
        'data/accommodation_exp.xml',

        'views/templates.xml',

        'views/rooms.xml',
        'views/room_facility.xml',
        'views/accommodation.xml',
        'views/partner.xml',
        'views/food_ordering.xml',
        'views/food_category.xml',
        'views/product.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
