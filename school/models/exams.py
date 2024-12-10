from odoo import fields,models

class Exams(models.Model):
    _name='odoo.exams'
    _description='Odoo Exams'

    name=fields.Char(string='Exam Name')
    student_id=fields.Many2one('odoo.school', string='Student', required=True)
    subject_id=fields.Many2one('school.subject', string='Subject', required=True)
    class_id=fields.Many2one('school.class', string='Class', required=True)
    date=fields.Date(string='Exam Date')
    marks_obtained = fields.Float(string='Marks Obtained')
    total_marks = fields.Float(string='Total Marks', default=100.0)