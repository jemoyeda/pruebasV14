from odoo import models, fields, api, _
from xml.dom import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    is_booking_order = fields.Boolean(string='Is Booking Order', default=True)
    team = fields.Many2one(comodel_name='service.team', string='Team')
    team_leader = fields.Many2one('res.users', string='Team Leader')
    team_members = fields.Many2many('res.users', string='Team Members')
    
    booking_start = fields.Date('Booking Start', default = lambda self:fields.Date.Today())
    booking_end = fields.Date(string='Booking End')

    field_name = fields.Char(compute='_compute_field_name', string='field_name')
    
    def _compute_field_name(self):
        wo_data = self.env['work.order'].sudo().read_group([('bo_reference', 'in', self.ids)],['bo_reference'],['bo_reference'])

        result = {
            data['bo_reference'][0]: data['bo_reference_count'] for data in wo_data
        }

        for a in self:
            a.wo_count = result.get(a.id, 0)

    @api.onchange('team')
    def _onchange_field(self):
        search = self.env['service.team'].search(['id', '=', self.team.id])
        team_members = []

        for team in search:
            team_members.extend(members.id for members in team.team_members)
            self.team_leader = team.team_leader.id
            self.team_members = team_members
    
    def check(self):
        for check in self:
            wo = self.env['work.order'].search(
                ['|', '|', '|',
                ('team_leader', 'in', [g.id for g in self.team_members]),
                ('team_members', 'in', [self.team_leader.id]),
                ('team_leader', '=', self.team_leader.id),
                ('team_members', 'in', [g.id for g in self.team_members]),
                ('state', '!=', 'cancelled'),
                ('planned_start', '<=', self.booking_end),
                ('planned_end', '>=', self.booking_start)],
                limit=1)
            if wo:
                raise ValidationError('Team already has work order during that period on %s', self.booking_start)
            else:
                raise ValidationError('Team is available for booking')

    def confirm(self):
        res = super(SaleOrder, self).confirm()
        for order in self:
            wo = self.env['work.order'].search(
                ['|', '|', '|',
                ('team_leader', 'in', [g.id for g in self.team_members]),
                ('team_members', 'in', [self.team_leader.id]),
                ('team_leader', '=', self.team_leader.id),
                ('team_members', 'in', [g.id for g in self.team_members]),
                ('state', '!=', 'cancelled'),
                ('planned_start', '<=', self.booking_end),
                ('planned_end', '>=', self.booking_start)],
                limit=1)
            if wo:
                raise ValidationError('Team is not available during this period, already booked on %s . Please book on another date.', self.booking_start)
            order.work_order_create()
        return res
    
    def work_order_create(self):
        wo_obj = self.env['work.order']
        for order in self:
            wo_obj.create([{
                'bo_reference': order.id,
                'team':order.team.id,
                'team_leader':order.team_leader.id,
                'team_members':order.team_members.ids,
                'planned_start':order.booking_start,
                'planned_end':order.booking_end}])
    
    
    
    
    
    
