from odoo import fields,models

class PropertyType(models.Model):
    _name="property.type"


    name=fields.Char(string="Type",required=True)
