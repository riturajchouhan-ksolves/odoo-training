# from email.policy import default

from odoo import fields,models,api

class PropertyWithPool(models.Model):
    _inherit='estate.property'

    has_pool=fields.Boolean(string="Has Pool",default=False)
