from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import date


class AllowedPeriod(models.Model):
    _name = 'allowed.period'
    _description = 'Model with Allowed Period Validation'
    # name = fields.Char(string='Name', required=True)

    name=fields.Char(string='Allowed Period Name', required=True)
    allowed_start_date = fields.Datetime(string='Allowed Start Date', default=fields.Datetime.now)
    allowed_end_date = fields.Datetime(string='Allowed end Date')


