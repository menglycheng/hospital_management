from odoo import api, fields, models, _


class Vaccine(models.Model):
    _name = 'vaccine.record'
    _description = 'Keep all vaccine record data'
    _rec_name = 'patient_id'

    vaccine_record = fields.Many2one('vaccine.data', 'vaccine_name')
    patient_id = fields.Many2one('patient.data','Patient Name')
    by_doctor = fields.Many2one('hr.employee', 'By Doctor')
    date = fields.Date("Date")


