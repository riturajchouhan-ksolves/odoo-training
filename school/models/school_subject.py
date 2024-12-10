from odoo import models,fields

class SchoolSubject(models.Model):
    _name='school.subject'

    name=fields.Char(string='Subject Name', required=True)
