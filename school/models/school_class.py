from odoo import models,fields

class SchoolClass(models.Model):
    _name='school.class'

    name = fields.Char(string='Class Name', required=True)
    student_ids = fields.One2many('odoo.school','class_id', string='Student')