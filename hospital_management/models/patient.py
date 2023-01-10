# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date


class PatientData(models.Model):
    _name = 'patient.data'
    _description = 'Keep all patient data'
    _rec_name = 'patient_name_eng'
    _order = 'reference DESC'

    reference = fields.Char('Reference', required=True, copy=False, readonly=True, default=lambda self: _("New"))
    patient_image = fields.Binary("Patient Image ")
    patient_name_eng = fields.Char('Patient Name English')
    patient_name_kh = fields.Char('Patient Name Khmer')
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')],
                              required=True, default='male')
    date_birth = fields.Date('Patient Date of Birth')
    patient_age = fields.Char('Age', compute="cal_age")
    patient_address = fields.Char("Patient's Address")
    patient_parent_name = fields.Char("Patient's Parent Name")
    patient_tel = fields.Char("Phone Number")

    appointment_count = fields.Integer('Appointment Total', compute='_compute_appointment_count')
    vaccine_count = fields.Integer('Vaccine Total', compute='_compute_vaccine_count')

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('patient.data') or _("New")
        res = super(PatientData, self).create(vals)
        return res

    @api.depends('date_birth')
    def cal_age(self):
        for rec in self:
            if rec.patient_age == "":
                rec.patient_age = "Null"
            if rec.date_birth:
                today = date.today()
                birthday = rec.date_birth

                ans = (today - birthday).days

                years = abs(ans // 365)
                months = (ans - years * 365) // 30
                days = (ans - years * 365 - months * 30)

                rec.patient_age = f'{years} years | {months} months | {days} days'

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = rec.env['patient.appointment'].search_count([('patient_id', '=', self.id)])
            rec.appointment_count = appointment_count

    def _compute_vaccine_count(self):
        for rec in self:
            vaccine_count = rec.env['vaccine.record'].search_count([('patient_id', '=', self.id)])
            rec.vaccine_count = vaccine_count
