from odoo import api, fields, models, _


class AppointmentData(models.Model):
    _name = 'patient.appointment'
    _description = 'Keep all patient appointment data'
    _rec_name = 'appointment_id'

    appointment_id = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True, default=lambda self: _("New"))
    patient_id = fields.Many2one('patient.data', string="Patient", required=True)
    appointment_date = fields.Date(string="Date", required=True)
    notes = fields.Text('Notes')
    height = fields.Float(string="height")
    by_doctor = fields.Many2one('hr.employee', 'by doctor')
    medicine_list = fields.One2many('invoice.record.line', 'appointment_id')
    usd_total_price = fields.Float('USD Total Price', compute="get_total_price")
    kh_total_price = fields.Float('KH Total Price', compute="get_total_price_kh")

    @api.model
    def create(self, vals):
        if vals.get('appointment_id', ('New')) == ('New'):
            vals['appointment_id'] = self.env['ir.sequence'].next_by_code('patient.appointment') or ('New')

        return super(AppointmentData, self).create(vals)

    @api.depends('medicine_list')
    def get_total_price(self):
        sum = 0
        for rec in self:
            for data in rec.medicine_list:
                sum += data.sub_price
            rec.usd_total_price = sum

    @api.depends('usd_total_price')
    def get_total_price_kh(self):
        for rec in self:
            rec.kh_total_price = rec.usd_total_price * 4100
