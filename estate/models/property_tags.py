from odoo import fields,models

class PropertyTags(models.Model):
    _name="property.tags"

    name=fields.Char(required=True)