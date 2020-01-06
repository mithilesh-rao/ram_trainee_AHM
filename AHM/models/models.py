from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api, exceptions

class Registration(models.Model):
    _name = 'ahm.registration'
    _description = 'AHM Registration'

    # reg_id = fields.One2many(comodel_name='AHM.Appointment',string="Select",ondelete="cascade")
    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image Upload")
    contact = fields.Char(string="Contact")
    email = fields.Char(string="Email", required=True)
    address = fields.Char(string="Address", required=True)
    visiting_time = fields.Datetime(string='Visiting Time')
    specialization = fields.Char(string="Specialization", required=True)
    degree_certificate  = fields.Binary(string="Degree Certificate")
    status = fields.Selection(selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done')],
        default='draft')

    def draft(self):
        self.write({"status": "draft"})

    def confirm(self):
        self.write({"status": "confirm"})

    def done(self):
        self.write({"status": "done"})

class Appointment(models.Model):
    _name  = 'ahm.appointment'
    _description = 'AHM Appointment'


    app_id = fields.Many2one(comodel_name='ahm.animal.registration',ondelete="cascade")
    name = fields.Char(string="Name", required=True)
    contact = fields.Char(string="Mobile No.", required=True)
    visiting_time = fields.Datetime(string='Visiting Time')
    visit_charges = fields.Integer(string="Visiting Charges", required=True)
    address = fields.Char(string="Address", required=True)

class AnimalRegistration(models.Model):
    _name = 'ahm.animal.registration'
    _description = "AHM Animal Registration"

    breed_name = fields.Char(string="Breed Name",required=True)
    breed_type = fields.Char(string="Breed Type", required=True)
    image = fields.Binary(string="Upload Image of the Breed")
    onwer_contact = fields.Integer(string="Mobile No.", required=True)
    email = fields.Char(string="Email", required=True)
    address = fields.Text(string="Address", required=True)

class OrganizationRegistration(models.Model):
    _name = 'ahm.organization.registration'
    _description = "AHM Organization Registration"

    org_name = fields.Char(string="Organization Name",required=True)
    org_registration_no = fields.Integer(string="Organization Registration Number", required=True)
    contact = fields.Integer(string="Mobile No.", required=True)
    email = fields.Char(string="Email", required=True)
    facility = fields.Text(string="Facility", required=True)
    address = fields.Text(string="Address",required=True)
    visiting_time = fields.Datetime(string="Visiting Time")
    helpline_number = fields.Integer(string="Helpline Number", required=True)

class Health(models.Model):
    _name = 'ahm.health'
    _description = "AHM Health"
    _rec_name = "duration"

    app_id = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")
    starting_date = fields.Date(string="Starting Date")
    ending_date = fields.Date(string="Ending Date")
    duration = fields.Integer(compute="_compute_duration")


    def _compute_duration(self):
        for i in self:
            delta = i.ending_date - i.starting_date
            i.duration = delta.days

class TotalCharges(models.Model):
    _name = 'ahm.total.charges'
    _description = "AHM Total Charges"

    app_id = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")
    medicine_charges = fields.Integer(string="Medicine Charges",required=True)
    other_charges = fields.Integer(string="Other Charges",required=True)
    total_bill = fields.Float(compute="_compute_total")

    @api.depends('medicine_charges','other_charges')
    def _compute_total(self):
      for ahm in self:
          ahm.total_bill = ahm.medicine_charges + ahm.other_charges
