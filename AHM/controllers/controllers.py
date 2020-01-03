from odoo import http

class AHM(http.controller):
	@http.route('/AHM/AHM', auth='Animal Health Monitering')
	def index(self, **kw):
		return "AHM"

class Appointment(http.controller):
	@http.route('/AHM/Appointment', auth='Animal Health Monitering')
	def index(self, **kw):
		return ""