from odoo import api, fields, models, _


class AppointmentData(models.Model):
    _name = 'patient.appointment'
    _description = 'Keep all patient appointment data'
    _rec_name = 'appointment_id'

    appointment_id = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True, default=lambda self: _("New"))
    patient_id = fields.Many2one('patient.data', string="Patient", required=True)
    appointment_date = fields.Date(string="Date", required=True)
    notes = fields.Text('Notes')


    @api.model
    def create(self, vals):
        if vals.get('appointment_id', ('New')) == ('New'):
            vals['appointment_id'] = self.env['ir.sequence'].next_by_code('patient.appointment') or ('New')

        return super(AppointmentData, self).create(vals)