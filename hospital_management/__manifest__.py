{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management',
    'sequence': 1,
    'description': " ",
    'category': 'Hospital',
    'website': '',

    'depends' : ['base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'menus/menu.xml',
        'wizard/create_appointment.xml',
        'views/resigter.xml',
        'views/appointment.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
