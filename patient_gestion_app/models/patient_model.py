from odoo import models, fields, api
import random
import string

class patientModel(models.Model):
    _name = 'patient_gestion_app.patient_model'
    _description = 'Patient Model'

    dni = fields.Char(string="Patient DNI", Required = True,index=True,help="DNI of the patient")
    name = fields.Char(string="Patient Name", Required = True,index=True,help="Name of the Patient")
    surname = fields.Char(string="Patient Surname", Required = True,index=True,help="Surname of the Patient")
    photo = fields.Binary(string="Photo")
    phone = fields.Char(string="Patient Phone", Required = True)
    birthday = fields.Date(string="Patient Birthday", Required = True)
    email = fields.Char(string="Patient Email", Required = True)
    visits = fields.One2many("patient_gestion_app.visits_model","patient", "Visits")

