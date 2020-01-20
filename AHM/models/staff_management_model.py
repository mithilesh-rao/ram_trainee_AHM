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
    contact = fields.Integer(string="Mobile No.", required=True)
    helpline_number = fields.Integer(string="Helpline Number")
    email = fields.Char(string="Email", required=True)
    facility = fields.Text(string="Facility", required=True)
    address = fields.Text(string="Address",required=True)
    opening_time = fields.Many2one(comodel_name="ahm.time",string="Clinic Opening Time")
    closing_time = fields.Many2one(comodel_name="ahm.time",string="Clinic Closing Time")
    workingdays = fields.Many2many(comodel_name="ahm.working.days", string="Working Days")

class WorkingDays(models.Model):
    _name = 'ahm.working.days'
    _description = "AHM Working Days"

    name = fields.Char(string="Week Day")


class Time(models.Model):
    _name = 'ahm.time'
    _description = "AHM Time"

    name = fields.Float(string="Time")
