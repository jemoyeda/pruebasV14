from odoo import api, fields, models, _


class WorkOrder(models.Model):
    _name = 'work.order'
    _description = 'Work Order'

    wo_number = fields.Char(string='WO Number', readonly=True, copy=False)
    bo_reference = fields.Many2one(comodel_name='sale.order', required=True)
    team = fields.Many2one(comodel_name='service_team', string='Team', required=True)
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader', required=True)
    team_members = fields.Many2many(comodel_name='res.users', string='Team Member')
    planned_start = fields.Datetime('Planned Start', required=True, default=lambda self: fields.Date.Today())
    planned_end = fields.Datetime('Planned End', required=True)
    date_start = fields.Datetime('Date Start', readonly=True)
    date_end = fields.Datetime('Date End', readonly=True)
    state = fields.Selection(string='State', selection=[
        ('pending', 'Pending'), 
        ('in progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
        ])
    notes = fields.Text(string='Notes')
    
    @api.model
    def create(self,values):
        if values.get('wo_number', _('New')) == _('New'):
            if 'company_id' in values:
                values['wo_number'] = self.env['ir.sequence'].with_context(
                    force_company=values['company_id']
                ).next_by_code('work.order') or _('New')
            else:
                values['wo_number'] = self.env['ir.sequence'].next_by_code(
                    'work.order'
                ) or _('New')
        
        return super(WorkOrder, self).create(values)

    def start_work(self):
        return self.write({'state': 'in_progress', 'date_start': field.Datetime.now()})

    def end_work(self):
        return self.write({'state': 'done', 'date_end': field.Datetime.now()})
        
    def reset(self):
        return self.write({'state': 'pending', 'date_start': ''})

    def cancel(self):
        return self.write({'state': 'cancel'})
        
                
                
    
    
    
