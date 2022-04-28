from odoo import models,fields

class RoomFacility(models.Model):
    _name = "hotel.room.facility"
    _description = "Hotel Room Facility"

    name = fields.Char(string="Facility")