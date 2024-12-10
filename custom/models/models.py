# -*- coding: utf-8 -*-
from tokenize import String

from odoo import models, fields
class hospitalProf(models.Model):
    _name:"custom.profile"

    name=fields.Char(String="Hospitalname")
    email=fields.Char(String="Email")


# class tutorial/custom(models.Model):
#     _name = 'tutorial/custom.tutorial/custom'
#     _description = 'tutorial/custom.tutorial/custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

