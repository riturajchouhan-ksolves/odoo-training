from odoo import fields, models, api
from odoo.exceptions import ValidationError

class AttributeAssignment(models.Model):
    _name='device.attribute.assignment'


    device_id=fields.Many2one('device.device',string='device',required=True,unique=True)
    device_attribute_id=fields.Many2one('device.attribute',string='Device Attribute',required=True)
    device_attribute_value_id=fields.Many2one('device.attribute.value',string='Device Attribute Value', required=True)

    @api.constrains('device_id', 'device_attribute_id')
    def _check_unique_device_attribute(self):
        for record in self:
            existing = self.search([
                ('device_id', '=', record.device_id.id),
                ('device_attribute_id', '=', record.device_attribute_id.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError(
                    f"The combination of Device and Device Attribute must be unique. "
                    f"This combination already exists."
                )