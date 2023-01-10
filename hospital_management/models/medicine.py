from odoo import api, fields, models, _


class Medicine(models.Model):
    _name = 'medicine.data'
    _description = 'Keep all medicine data'
    _rec_name = 'medicine_name'

    medicine_name = fields.Char('Medicine Name')
    sale_price = fields.Float('Sale Price')
    cost = fields.Float('Cost')
    units = fields.Char('Units On Hand')

    def test(self):
        print('Hello')