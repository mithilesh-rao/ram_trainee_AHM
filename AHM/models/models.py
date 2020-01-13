from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo import models, fields, api, exceptions


class Health(models.Model):
    _name = 'ahm.health'
    _description = "AHM Health"
    _rec_name = "duration"

    app_id = fields.Many2one(comodel_name="ahm.appointment",ondelete="cascade")
    starting_date = fields.Date(string="Starting Date")
    ending_date = fields.Date(string="Ending Date")
    duration = fields.Integer(compute="_compute_duration")
    graph_field = fields.Float("Graph")


    def _compute_duration(self):
        for i in self:
            if i.ending_date and i.starting_date:
                delta = i.ending_date - i.starting_date
                i.duration = delta.days
            else:
                i.duration = 2
                