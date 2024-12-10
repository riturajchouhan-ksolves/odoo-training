from odoo import models, fields

class TestModel(models.Model):
    _inherit='school.class'

    teacher_id=fields.Many2one('hr.employee',string='Teachers',domain=[('is_teacher','=', True)])