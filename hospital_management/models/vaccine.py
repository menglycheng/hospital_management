from odoo import api, fields, models, _


class Vaccine(models.Model):
    _name = 'vaccine.data'
    _description = 'Keep all vaccine data'
    _rec_name = 'vaccine_name'

    vaccine_name = fields.Char('Vaccine Name')

    def test(self):
        print('Hello')

class VaccineStock(models.Model):
    _name = 'vaccine.data.stock'
    _description = 'Keep all vaccine data stock'
    _rec_name = ''

    vaccine_name = fields.Many2one('vaccine.data','Vaccine Name')
    units = fields.Integer('Unit')

