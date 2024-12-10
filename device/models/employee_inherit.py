
from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    name=fields.Char('Employee Name',required=True)
    device_assignment_ids = fields.One2many('device.assignment', 'employee_id', string="Device Assignments")
    device_ids = fields.Many2many('device.device', string="Devices")