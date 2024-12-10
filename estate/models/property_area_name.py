from odoo import fields,models

class PropertyArea(models.Model):
    _name="property.area.area"

    name=fields.Char(string="empty property area name")
    property_name_area_id=fields.Many2one("estate.property",string="area name")