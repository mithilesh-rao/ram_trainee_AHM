from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api, exceptions



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
