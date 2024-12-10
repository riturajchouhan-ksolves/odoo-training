from odoo import fields,models

class GenerateReport(models.Model):
    _name='generate.report'
    _description='Hey'

    student_id=fields.Many2one('odoo.school',string='Enter Student Name',required=True)

    def action_report_exam_marks(self):
        return self.env.ref('school.action_report_exam_marks').report_action(self)