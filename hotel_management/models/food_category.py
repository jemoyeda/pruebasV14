from odoo import models,fields,api,tools,_

class FoodCategory(models.Model):

    _name = 'hotel.food.category'
    _description = 'Food Category'

    name = fields.Selection([
        ('breakfast', 'Brekfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
        ('hot_drink','Hot Drink'),
        ('cool_drink','Cool Drink')
    ],string='Category')
    product_ids = fields.Many2many('product.product', string='Items')


    @api.onchange('product_ids')
    def _onchange_product_ids(self):
        obj = self.env['product.product']
        self.ensure_one()
        print("product id")
        print(self.product_ids.ids)
        for pro_id in self.product_ids.ids:
            pro_rec = obj.search([('id','=',pro_id)])
            pro_rec.category_id = self.ids[0]


