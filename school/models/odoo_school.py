from odoo import fields,models

class TestModel(models.Model):
    _name = "odoo.school"
    _description = 'Odoo School Project'

    name=fields.Char(string="Student Name", required=True)
    dob=fields.Date(string="Date of birth",required=True)
    class_id = fields.Many2one('school.class', string='Class')
    subject_ids=fields.Many2many('school.subject',string='Subjects')
    fee_ids=fields.One2many('school.fee','student_id',string='Fees')

    exams=fields.One2many('odoo.exams','student_id',string="Exams")


