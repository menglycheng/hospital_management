from odoo import api, fields , models,_


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create appointment wizard'

    patient_id = fields.Many2one('patient.data', string='Patient Id')
    appointment_date = fields.Date('Appointment Date')
    note = fields.Text('Note')

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': self.note
        }
        self.env['patient.appointment'].create(vals)

