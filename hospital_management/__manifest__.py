{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management',
    'sequence': 1,
    'description': " ",
    'category': 'Hospital',
    'website': '',

    'depends' : ['base_setup','hr'],
    'data': [
        'security/ir.model.access.csv',
        'menus/menu.xml',
        'data/data.xml',
        'wizard/create_appointment.xml',
        'views/resigter.xml',
        'views/appointment.xml',
        'views/vaccine.xml',
        'views/medicine.xml',
        'views/vaccine_record.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
