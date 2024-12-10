from odoo import fields, models, api
from odoo.exceptions import ValidationError

class DeviceAttributeValue(models.Model):
    _name='device.attribute.value'

    name=fields.Char('Name',required=True,unique=True, translate=True)
    device_attribute_id=fields.Many2one('device.attribute',string='Device Attribute',required=True)

    @api.constrains('name', 'device_attribute_id')
    def _check_unique_name_device_attribute(self):
        for record in self:
            existing = self.search([
                ('name', '=', record.name),
                ('device_attribute_id', '=', record.device_attribute_id.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError(
                    f"The combination of Name and Device Attribute must be unique. "
                    f"'{record.name}' already exists for this Device Attribute."
                )