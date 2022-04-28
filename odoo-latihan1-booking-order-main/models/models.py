# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class angel_booking_order(models.Model):
#     _name = 'angel_booking_order.angel_booking_order'
#     _description = 'angel_booking_order.angel_booking_order'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
