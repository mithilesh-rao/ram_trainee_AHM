from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api


class AnimalRegistration(models.Model):
    _name = 'ahm.animal.registration'
    _description = "AHM Animal Registration"

    breed_name = fields.Char(string="Breed Name",required=True)
    breed_type = fields.Char(string="Breed Type", required=True)
    image = fields.Binary(string="Upload Image of the Breed")
    onwer_contact = fields.Integer(string="Mobile No.", required=True)
    email = fields.Char(string="Email", required=True)
    address = fields.Text(string="Address", required=True)

class Appointment(models.Model):
    _name  = 'ahm.appointment'
    _description = 'AHM Appointment'

    # app_id = fields.(comodel_name='ahm.animal.registration',ondelete="cascade")
    name = fields.Char(string="Name", required=True)
    contact = fields.Char(string="Mobile No.", required=True)
    visiting_date = fields.Date(string="Appointment Date")
    visiting_time = fields.Many2one(comodel_name="ahm.time", string='Appointment Time')
    visit_charges = fields.Integer(string="Visiting Charges")
    address = fields.Char(string="Address", required=True)

    @api.onchange("visiting_date")
    def visitingtime(self):
        time_env = self.env['ahm.time'].search([])
        appointment = self.env['ahm.appointment'].search([])
        appointment_env = self.env['ahm.appointment'].search([('visiting_date','=',self.visiting_date)])
        print("-----------------------", appointment_env.visiting_time.ids)
        return {'domain' : {'visiting_time' : [('id','not in', appointment_env.visiting_time.ids)]}}

 
class PatientDetail(models.Model):
    _name = 'ahm.patient.detail'
    _description = "AHM Patient Detail"

    app_id = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")
    name = fields.Char(string="Name", required=True)
    medicine = fields.Text(String="Medicine")
    prescription = fields.Char(string="Prescription")
    image = fields.Binary(string="Image",attachment=True)

class BreedType(models.Model):
    _name = 'ahm.breed.type'
    _description = "AHM Breed Type"

    b_type = fields.Selection(string="Select Breed Type",
        selection=[('cow', 'Cow'), 
        ('dog', 'Dog'), 
        ('cat', 'Cat'),
        ('horse','Horse'),
        ('buffalo','Buffalo'),
        ('rabbit','Rabbit')],
        default='dog')