from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Device(models.Model):
    _name='device.device'

    name=fields.Char(string=('Name'), required=True,unique=True,translate=True)
    shared=fields.Boolean('Shared',default=False)
    device_type_id=fields.Many2one('device.type',string='Device Type')
    device_brand_id=fields.Many2one('device.brand',string='Device Brand')
    device_model_id=fields.Many2one('device.model',string='Device Model')
    device_attribute_ids=fields.One2many('device.attribute.assignment','device_id',string='Attribute')

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if existing:
                raise ValidationError(f"The name '{record.name}' must be unique.")