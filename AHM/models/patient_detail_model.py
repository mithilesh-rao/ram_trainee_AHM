from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api, exceptions


class PatientDetail(models.Model):
    _name = 'ahm.patient.detail'
    _description = "AHM Patient Detail"

    app_id = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")
    name = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")
    medicine = fields.Text(String="Medicine",required=True)
    prescription = fields.Char(string="Prescription")
    image = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")

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
 