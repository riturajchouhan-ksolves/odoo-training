from dateutil.relativedelta import relativedelta
from odoo import fields,models,api
from datetime import datetime,date


from  odoo.exceptions import ValidationError, UserError

from odoo17.odoo.cli.scaffold import template
from odoo17.odoo.tools.populate import compute


class TestModel(models.Model):
    _name="estate.property"
    _description='Real estate project'
    _inherit=['mail.thread','mail.activity.mixin']
    _rec_name = 'property_reference'
    property_type_id=fields.Many2one('property.type')
    property_tags_ids=fields.Many2many('property.tags',string="Tags")
    property_area_ids=fields.One2many("property.area.area","property_name_area_id",string="Area")
    fname=fields.Char(string="Owner's firstname",required=True)
    lname=fields.Char(string="owner's lastname",required=True)
    status=fields.Char(string="Property's status")
    state=fields.Selection(
        [
            ('draft','Draft'),
            ('active','Active'),
            ('sold','Sold'),

        ],
        string="State",
        default='draft',
        required=True,
    )
    gender=fields.Selection(
        [
            ('female','Female'),
            ('male','Male'),
        ],
        string="Gender",
        default='female',
        required=True
    )
    age=fields.Integer(string="Age",compute="compute_age")
    date_of_birth=fields.Date(string="DOB",required=True)
    total_area=fields.Float(string="total_area")
    price_per_sqft=fields.Float(string="price_per_sqft")
    total_price=fields.Float(string="total_price")
    property_reference = fields.Char(string="Property Reference", readonly=True, copy=False)
    is_active = fields.Boolean(string="Is Active",default=True, readonly=True)


    @api.model
    def write(self, vals):
        current_date = datetime.now().date()
        allowed_periods = self.env['allowed.period'].search([
            ('allowed_start_date', '<=', current_date),
            ('allowed_end_date', '>=', current_date)
        ])
        if not allowed_periods:
            raise UserError('You can only edit this property within an allowed period.')
        return super(TestModel, self).write(vals)

    @api.depends("date_of_birth")
    def compute_age(self):
        for record in self:
            record.age=relativedelta(date.today(),record.date_of_birth).years

    @api.onchange("total_area","price_per_sqft")
    def _onchange_price_persqft(self):
        for records in self:
            if records.total_area > 0 and records.price_per_sqft > 0:
                records.total_price = records.total_area * records.price_per_sqft
            else:
                records.total_price=0


    @api.constrains('total_area')
    def check_area(self):
        for record in self:
            if(record.total_area<0):
                raise UserError("Amount Must be Positive")


    @api.constrains('price_per_sqft')
    def check_price(self):
        for record in self:
            if(record.price_per_sqft<0):
                record.price_per_sqft = 0
                raise UserError("Please Enter Positive Amount")

    @api.model
    def create(self, vals):
        if 'property_reference' not in vals:
            sequence = self.env['ir.sequence'].next_by_code('estate.property.sequence')
            if not sequence:
                raise UserError("No sequence found for property reference.")
            vals['property_reference'] = sequence

            current_date = datetime.now().date()
            allowed_periods = self.env['allowed.period'].search([
                ('allowed_start_date', '<=', current_date),
                ('allowed_end_date', '>=', current_date)
            ])
            if not allowed_periods:
                raise UserError('You can only create this property within an allowed period.')


        return super(TestModel, self).create(vals)

    def action_do_book(self):
        for record in self:
            record.status="Booked"
            # return True

    def action_do_cancel(self):
        for record in self:
            if(record.status=="Booked"):
                raise UserError("Booked properties cannot be cancelled")
            else:
                record.status="Cancelled"
                return True

    _sql_constraints = [
        ('check_total_area_positive', 'CHECK(total_area >= 0)', 'Total area must be positive.'),
        ('check_price_per_sqft_positive', 'CHECK(price_per_sqft >= 0)', 'Price per square foot must be positive.')
    ]

    def change_status(self):
        properties = self.env['estate.property'].search([('status', '=', 'Cancelled')])
        properties.write({'is_active': False})

    @api.model
    def action_cron_send_reminder(self):
        template = self.env.ref('estate_property.email_template_reminder')
        partners = self.env['res.partner'].search([('email', '!=', False)])
        for partner in partners:
            template.send_mail(partner.id, force_send=True)

        return True