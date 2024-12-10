from odoo import fields, models, api
from odoo.exceptions import ValidationError
class DeviceModel(models.Model):
    _name='device.model'

    name=fields.Char('Name',required=True,unique=True,translate=True)
    device_type_id=fields.Many2one('device.type',string='Device Type',required=True)
    device_brand_id=fields.Many2one('device.brand',string='Device Brand',required=True)

    @api.constrains('name', 'device_type_id', 'device_brand_id')
    def _check_unique_name_device_type_brand(self):
        for record in self:
            existing = self.search([
                ('name', '=', record.name),
                ('device_type_id', '=', record.device_type_id.id),
                ('device_brand_id', '=', record.device_brand_id.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError(
                    'The combination of Name, Device Type, and Device Brand must be unique.'
                )

