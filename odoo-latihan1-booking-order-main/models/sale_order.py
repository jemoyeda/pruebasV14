from odoo import api, fields, models


class Sale_Order(models.Model):
    _name = 'bo.saleorder'
    _description = 'New Description'

    name = fields.Char(string='Name',
                        readonly=True, 
                        required=True,
                        copy=False,
                        default='New')
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('so.number') or 'New'
        result = super(Sale_Order, self).create(vals)
        return result

    is_booking_order = fields.Boolean(string='Is Booking Order?', default=True)
    
    team = fields.Many2one(comodel_name='bo.serviceteam', 
                        string='Team', 
                        required=True)

    team_leader = fields.Many2one(comodel_name='res.users', 
                                string='Team Leader', 
                                required=True,
                                compute='_compute_team_leader')
    @api.depends('team')
    def _compute_team_leader(self):
        for record in self:
            record.team_leader = record.team.team_leader
    
    team_members = fields.Many2many(comodel_name='res.users', 
                                string='Team Members', 
                                required=True,
                                compute='_compute_team_members')
    @api.depends('team')
    def _compute_team_members(self):
        for record in self:
            record.team_members = record.team.team_members

    booking_start = fields.Datetime('Booking Start', required=True)
    booking_end = fields.Datetime('Booking End', required=True)
    
    
    
    
