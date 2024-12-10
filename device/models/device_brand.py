from odoo import fields, models,api
from odoo.exceptions import ValidationError

class DeviceBrand(models.Model):
    _name='device.brand'

    name=fields.Char('Name',required=True,unique=True, translate=True)
    device_models_ids=fields.One2many('device.model','device_brand_id', string='Device Models')

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            existing = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if existing:
                raise ValidationError(f"The Device Brand name '{record.name}' must be unique.")