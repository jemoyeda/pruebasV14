from datetime import datetime
from tkinter import HIDDEN
from xmlrpc.client import DateTime
from odoo import api, fields, models


class WorkOrder(models.Model):
    _name = 'bo.workorder'
    _description = 'New Description'

    # wo number
    name = fields.Char(string="WO Number", 
                        readonly=True, 
                        required=True,
                        copy=False,
                        default='New')
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('wo.number') or 'New'
        result = super(WorkOrder, self).create(vals)
        return result

    booking_order_reference = fields.Many2one(comodel_name='bo.saleorder', 
                                            string='Booking Order Reference',
                                            readonly=True)
                                            # autofilled?
    
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
                        compute='_compute_team_members')
    @api.depends('team')
    def _compute_team_members(self):
        for record in self:
            record.team_members = record.team.team_members
    
    planned_start = fields.Datetime('Planned Start', required=True)
    planned_end = fields.Datetime('Planned End', required=True)
    
    date_start = fields.Datetime('Date Start', readonly=True)
    date_end = fields.Datetime('Date End', readonly=True)
    
    state = fields.Selection([
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State')

    def btn_start_work(self):
        self.state = "in progress"
        self.date_start = datetime.now()

    def btn_end_work(self):
        self.state = "done"
        self.date_end = datetime.now()

    def btn_reset(self):
        self.state = "pending"
        self.date_start = ""
    
    def btn_cancel(self):
        self.state = "cancelled"
    
    # textarea
    notes = fields.Text('Notes')
    
    
    
    
    
