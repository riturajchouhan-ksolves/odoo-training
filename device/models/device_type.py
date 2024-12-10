from odoo import fields, models, api
from odoo.exceptions import ValidationError

class DeviceType(models.Model):
    _name='device.type'

    name=fields.Char(string='Name',required=True,unique=True, translate=True)
    code=fields.Char(string='Code',required=True,unique=True)
    sequence=fields.Integer('Sequence')
    device_attribute_ids=fields.Many2many('device.attribute','device_type_device_attribute_rel','device_type_id','device_attribute_id',string='Device Attributes')
    device_model_ids=fields.Many2many('device.model','device_type_device_model_rel','device_type_id','device_model_id',string='Device Model')
    device_ids=fields.One2many('device.device','device_type_id',string='Devices')

    @api.constrains('name', 'code')
    def _check_unique_name_and_code(self):
        for record in self:
            existing = self.search([
                ('name', '=', record.name),
                ('code', '=', record.code)
            ])
            if len(existing) > 1 or (len(existing) == 1 and existing.id != record.id):
                raise ValidationError(
                    'The combination of Name and Code must be unique.'
                )