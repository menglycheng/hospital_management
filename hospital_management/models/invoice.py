from odoo import api, fields, models, _


class InvoiceRecord(models.Model):
    _name = 'invoice.record.line'
    _description = 'Keep all patient invoice record data'
    _rec_name = ''

    medicine_id = fields.Many2one('medicine.data', 'Medicine Name')
    medicine_qty = fields.Integer('Quality')
    unit_price = fields.Float('Unit Price', compute="get_price")
    sub_price = fields.Float('Sub Price', compute="cal_total_price")
    appointment_id = fields.Many2one('patient.appointment', string='Appointment')

    @api.depends('medicine_qty','unit_price')
    def cal_total_price(self):
        for rec in self:
            rec.sub_price = rec.medicine_qty * rec.unit_price

    @api.depends('medicine_id')
    def get_price(self):
        for rec in self:
            rec.unit_price = rec.medicine_id.sale_price