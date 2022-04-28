from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender')
    accommodation_id = fields.Many2one('hotel.accommodation', string='Accommodation')


class PartnerLine(models.Model):
    _name = 'hotel.partner.lines'
    _description = 'hotel Partner Line'

    partner_id = fields.Many2one('res.partner',string='Name')
    accommodation_id = fields.Many2one('hotel.accommodation', string='Accommodation')
    age = fields.Integer(string='Age', related='partner_id.age')
    gender = fields.Selection(related='partner_id.gender')

