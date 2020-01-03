from odoo import models, fields

class Registration(models.Model):
	_name = 'ahm.registration'
	_description = 'AHM Registration'

	name = fields.Char(string="Name", required=True)
	image = fields.Binary(string="Image Upload")
	contact = fields.Char(string="Contact")
	email = fields.Char(string="Email", required=True)
	address = fields.Char(string="Address", required=True)
	visiting_time = fields.Datetime(string='Visiting Time', required=True)
	specialization = fields.Char(string="Specialization", required=True)
	degree_certificate  = fields.Binary(string="Degree Certificate")

class Appointment(models.Model):
	_name  = 'ahm.appointment'
	_description = 'AHM Appointment'

	app_id = fields.Many2one(comodel_name='AHM.Animal_Registration',invisible=True,ondelete="cascade")
	name = fields.Char(string="Name", required=True)
	contact = fields.Char(string="Mobile No.", required=True)
	visiting_time = fields.Datetime(string='Visiting Time')
	visit_charges = fields.Integer(string="Visiting Charges", required=True)
	address = fields.Char(string="Address", required=True)

class Animal_Registration(models.Model):
	_name = 'ahm.animal_registration'
	_description = "AHM Animal_Registration"

	breed_name = fields.Char(string="Breed Name",required=True)
	breed_type = fields.Char(string="Breed Type", required=True)
	image = fields.Binary(string="Upload Image of the Breed")
	onwer_contact = fields.Integer(string="Mobile No.", required=True)
	email = fields.Char(string="Email", required=True)
	address = fields.Text(string="Address", required=True)

class Organization_Registration(models.Model):
	_name = 'ahm.organization_registration'
	_description = "AHM Organization_Registration"

	org_name = fields.Char(string="Organization Name",required=True)
	org_registration_no = fields.Integer(string="Organization Registration Number", required=True)
	contact = fields.Integer(string="Mobile No.", required=True)
	email = fields.Char(string="Email", required=True)
	facility = fields.Text(string="Facility", required=True)
	address = fields.Text(string="Address",required=True)
	visiting_time = fields.Datetime(string="Visiting Time", required=True)
	helpline_number = fields.Integer(string="Helpline Number", required=True)
