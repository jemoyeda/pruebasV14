from odoo import models, fields, tools, _, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError




class Accommodation(models.Model):
    _name = 'hotel.accommodation'
    _inherit = ['mail.thread']
    _description = 'Hotel Accommodation'

    name = fields.Char(string='Accommodation Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Guest', required=True)
    no_guests = fields.Integer(string='Number of Guests', required=True)

    check_in_date = fields.Date(string='Check in date', required=True,default=datetime.now())
    check_out_date = fields.Date(string='Check out date', required=True,dafault=datetime.now())
    bed_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('dormitory', 'Dormitory')
    ], string='Bed type', reuired=True)
    facility_ids = fields.Many2many('hotel.room.facility', string='Room Facility')
    room_id = fields.Many2one('hotel.rooms', string='Room', domain="[('check_in_state','!=','True')]")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('check_in', 'Check in'),
        ('check_out', 'check out'),
        ('cancel', 'Cancel')
    ], string='State', default='draft', readonly=True)

    expected_days = fields.Integer(string="Expected Days")
    expected_date = fields.Date(string='Expected Date', compute='_compute_expected_date', default=datetime.now())
    next_day_check_out_date = fields.Date(compute='_next_day_check_out_date')
    today_date = fields.Date(default=datetime.now())
    partner_ids = fields.One2many('hotel.partner.lines', 'accommodation_id', string='Guest information')

    @api.depends("check_in_date", "expected_days")
    def _compute_expected_date(self):
        for rec in self:
            if rec.check_in_date and rec.expected_days >= 0:
                modified_date = (rec.check_in_date) + timedelta(days=(rec.expected_days))
                rec.expected_date = datetime.strftime(modified_date, "%Y-%m-%d")
                print("EXPECTED DATE")
                print(rec.expected_date)
                print(rec.today_date)


    def _next_day_check_out_date(self):
        for rec in self:
            modified_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            rec.next_day_check_out_date = modified_date

    def action_check_in(self):
        print("Check in")
        obj = self.env['hotel.rooms']
        self.ensure_one()
        if len(self.partner_ids) == self.no_guests:
            self.write({'state': 'check_in'})
            self.update({'check_in_date': datetime.now()})

            rec = obj.search([('id', '=', self.room_id.id)])
            rec.update({'check_in_state': True})
        else:
           raise UserError(_('Please provide all guest details'))



    def action_check_out(self):
        print("Check out")
        obj = self.env['hotel.rooms']
        self.ensure_one()

        self.write({'state': 'check_out'})
        self.update({'check_out_date': datetime.now()})

        rec = obj.search([('id', '=', self.room_id.id)])
        rec.update({'check_in_state': False})


    def action_cancel(self):
        print('Cancel')
        self.write({'state':'cancel'})

    @api.model
    def create(self, val):
        if val.get('name', _('New')) == _('New'):
            val['name'] = self.env['ir.sequence'].next_by_code('hotel.accommodation') or _('New')
        res = super(Accommodation, self).create(val)
        return res

    @api.onchange('expected_date')
    def _onchange_expected_date(self):
        self.update({'today_date': self.expected_date})


    @api.model
    def _cron_job_acccommodation(self):
        print("Cron job")
        # obj = self.env['hotel.accommodation']
        # self.ensure_one()
        recs  = self.search([('state', '=', 'check_out')])
        print(recs)
        if recs:
            recs.unlink()
