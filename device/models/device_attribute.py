from odoo import fields, models, api
from odoo.exceptions import ValidationError

class DeviceAttribute(models.Model):
    _name='device.attribute'


    name=fields.Char('Name',required=True,unique=True,translate=True)
    device_type_id=fields.Many2one('device.type',string='Device Type', required=True)
    required=fields.Boolean('Required',default=False)
    device_attribute_value_ids = fields.Many2many('device.attribute.value', 'device_attribute_device_attribute_value_rel', 'device_attribute_id', 'device_attribute_value_id',
        string='Device Attribute Values' )

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if existing:
                raise ValidationError(f"The Device Attribute name '{record.name}' must be unique.")