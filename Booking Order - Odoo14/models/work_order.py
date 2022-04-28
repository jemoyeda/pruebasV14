from odoo import api, fields, models
from datetime import *

class SaleWorkOrder(models.Model):
    _name = 'sale.work.order'
    _description = 'Sale Work Order'

    name = fields.Char(string='WO Number', readonly=True, default='New', required=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Booking Order Ref')
    
    team_id = fields.Many2one(comodel_name='service.team', string='Service Team', required=True)
    team_leader_id = fields.Many2one(comodel_name='res.users', string='Service Team Leader', required=True)
    team_member_ids = fields.Many2many(comodel_name='res.users', string='Service Members', required=True)
    
    @api.onchange('team_id')
    def onchange_team_id(self):
        for record in self:
            record.team_leader_id = record.team_id.team_leader_id
            record.team_member_ids = record.team_id.team_member_ids
    
    planned_start = fields.Datetime(string='Planned Start', default=datetime.today(), required=True)

    @api.onchange('planned_start')
    def onchange_planned_start(self):
        for record in self:
            record.planned_end = record.planned_start + timedelta(days=1)
            
    planned_end = fields.Datetime(string='Planned End', default=datetime.today() + timedelta(days=1), required=True)
    
    @api.onchange('planned_end')
    def onchange_planned_end(self):
        for record in self:
            record.planned_start = record.planned_end - timedelta(days=1)
            
    date_start = fields.Datetime(string='Date Start', readonly=True)
    date_end = fields.Datetime(string='Date End', readonly=True)
    state = fields.Selection(string='Status', selection=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancel', 'Cancel')], readonly=True, default='pending', required=True)
    
    notes = fields.Text(string='Notes')
    