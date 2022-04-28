from odoo import models,fields,api,tools,_
from datetime import datetime


class OrderFood(models.Model):

    _name = 'hotel.food.order'
    _description = 'Food Ordering'

    name = fields.Many2one('hotel.rooms',string="Rooms", domain="[('check_in_state','=',True)]",required=True)
    guest_name = fields.Char(string='Guest')
    order_time = fields.Datetime(string='Ordering Date', default=datetime.now(),readonly=True)
    food_category_ids = fields.Many2many('hotel.food.category')
    product_ids = fields.Many2many('product.product')


    @api.onchange('name','food_category_ids')
    def _onchage_name(self):
        obj = self.env['hotel.accommodation']
        # pro_obj = self.env['product.product']

        self.ensure_one()
        print('guest')
        for rec in self:
            if rec.name:
                acc_rec = obj.search([('room_id','=',rec.name.id)])
                print(acc_rec.partner_id)
                rec.write({'guest_name': acc_rec.partner_id.name})

            prdct_ids = []
            for i in rec.food_category_ids.product_ids:
                print(i.ids[0])
                prdct_ids.append(i.ids[0])

                # pro_rec = pro_obj.search([('id','=',i.ids[0])])
                # pro_rec.update({'category_id': 1})

            domain = {'product_ids': [('id', 'in', prdct_ids)]}
            return {'domain': domain, 'value': {'product_ids': []}}