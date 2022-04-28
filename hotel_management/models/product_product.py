from odoo import fields,models,tools,api,_


class Products(models.Model):
    _inherit = 'product.product'

    category_id = fields.Many2one('hotel.food.category',string='Food Category')