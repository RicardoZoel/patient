from odoo import models, fields, api
import random
import string

class visitsModel(models.Model):
    _name = 'patient_gestion_app.visits_model'
    _description = 'Visits Model'

    patient = fields.Many2one("patient_gestion_app.patient_model", "Patient")
    data = fields.Date(string="Patient Birthday", Required = True)
    detall = fields.Html("Description", Required = True)

