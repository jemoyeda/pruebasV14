from odoo import fields, models, tools,api


class Rooms(models.Model):
    _name = "hotel.rooms"
    _description = "Hostel Rooms"

    name = fields.Char(string='Room Number')
    bed = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('dormitory', 'Dormitory')
    ])
    available_beds = fields.Integer(string="Available Beds")
    room_facility_ids = fields.Many2many('hotel.room.facility', string="Room Facilities")
    currency_id = fields.Many2one('res.currency', string='Currency')
    rent = fields.Monetary(string='Rent')

    check_in_state = fields.Boolean(default=False)

    tag_id_custom = fields.Char(string='Tags', compute='_get_tags', store=True)

    @api.model
    @api.depends('room_facility_ids')
    def _get_tags(self):
        for rec in self:
            if rec.room_facility_ids:
                tag_custom = ','.join([p.name for p in rec.room_facility_ids])
                print("tag_custom")
                print(tag_custom)
            else:
                tag_custom = ''
            rec.tag_id_custom = tag_custom

