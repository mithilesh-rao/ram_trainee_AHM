from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api, exceptions

class Registration(models.Model):
    _name = 'ahm.registration'
    _description = 'AHM Registration'

    name = fields.Char(required=True)
    image = fields.Binary(required=True)
    contact = fields.Char(string="Contact")
    email = fields.Char(string="Email", required=True)
    address = fields.Char(string="Address", required=True)
    visiting_time = fields.Datetime(string='Visiting Time')
    specialization = fields.Char(string="Specialization", required=True)
    degree_certificate  = fields.Binary()
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done')], default='draft')

    def draft(self):
        self.write({"status": "draft"})

    def confirm(self):
        self.write({"status": "confirm"})

    def done(self):
        self.write({"status": "done"})

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
