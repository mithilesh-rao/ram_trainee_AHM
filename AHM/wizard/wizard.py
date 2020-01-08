from odoo import models, fields, api

class Stock(models.TransientModel):
	_name = 'ahm.stock'
	_description = "AHM Stock"


	name = fields.Char(string="Stock Name")
	comp = fields.Char(string="Comapny")