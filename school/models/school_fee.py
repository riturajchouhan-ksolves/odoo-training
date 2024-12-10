from odoo import models,fields

class SchoolFee(models.Model):
    _name='school.fee'
    _description='Fee'

    name=fields.Char(string="Fees Description")
    month = fields.Selection([
        ('jan', 'January'),
        ('feb', 'February'),
        ('mar', 'March'),
        ('apr', 'April'),
        ('may', 'May'),
        ('jun', 'June'),
        ('jul', 'July'),
        ('aug', 'August'),
        ('sep', 'September'),
        ('oct', 'October'),
        ('nov', 'November'),
        ('dec', 'December'),
    ], string='Month', required=True)
    amount=fields.Float(string='Amount',required=True)
    student_id = fields.Many2one('odoo.school', string='Student')