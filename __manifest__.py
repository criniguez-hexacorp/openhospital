# -*- coding: utf-8 -*-
{
    'name': "Open Hospital",

    'summary': """Module for managing hospitals""",

    'description': """Module for managing hospitals""",

    'author': "Cristian Iñiguez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/openhospital_menus.xml',
        'views/openhospital_patient_views.xml',
        'views/openhospital_appointment_views.xml',
        'views/sale_order_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False
}
