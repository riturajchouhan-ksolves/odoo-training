from odoo import fields, models, api,_
from odoo.exceptions import ValidationError

class DeviceAssignment(models.Model):
    _name='device.assignment'

    name = fields.Char('Name / Code', required=True, unique=True,translate=True)
    device_id = fields.Many2one(
        'device.device',
        string='Device',
        required=True
    )
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date_start = fields.Date('Start Date', required=True)  #  start date
    date_expire = fields.Date('Expire Date')
    state = fields.Selection(
        [('new', _('New')),
         ('draft', _('Draft')),
         ('approved', _('Approved')),
         ('returned', _('Returned')),
         ('rejected', _('Rejected'))],
        string='State',
        default='new',
        required=True
    )


    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if existing:
                raise ValidationError(f"The name '{record.name}' must be unique.")