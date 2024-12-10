from odoo import fields,models


class CreateExamWizard(models.TransientModel):
    _name = 'create.exam.wizard'
    _description = 'Wizard to Create Exams'

    exam_name = fields.Char(string='Exam Name', required=True)
    date =fields.Date(string='Exam Date',required=True)
    student_id=fields.Many2one('odoo.school',string='Student',required=True)
    class_id=fields.Many2one('school.class',string='Class',required=True)

    def create_exams(self):
        students=self.env['odoo.school'].search([])
        subjects=self.env['school.subject'].search([])
        exam_obj=self.env['odoo.exams']

        for student in students:
            for subject in subjects:
                exam_obj.create({
                    'name':self.exam_name,
                    'student_id':student.id,
                    'subject_id':subject.id,
                    'date':self.date,
                    'total_marks':100,
                    'class_id':self.class_id.id
                })
        return {'type': 'ir.actions.client', 'tag': 'reload'}


    def print_exam_report(self):
        students=self.env['odoo.school'].search([('class_id','=',self.class_id.id)])
        data = {
            'exam_name': self.exam_name,
            'students':students
        }
        return self.env.ref('school.action_report_exam_marks').report_action(self,data=data)