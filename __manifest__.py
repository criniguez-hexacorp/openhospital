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
    'depends': [
        'base', 'mail', 'sale',
        'report_xlsx'  # https://apps.odoo.com/apps/modules/13.0/report_xlsx/
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/openhospital_security.xml',

        'reports/openhospital_patient_templates.xml',
        'reports/openhospital_patient_reports.xml',

        'data/ir_cron_data.xml',
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'data/openhospital_patient_data.xml',
        'data/openhospital_appointment_data.xml',

        'wizard/openhospital_appointment_create.xml',

        'views/openhospital_menus.xml',
        'views/openhospital_patient_views.xml',
        'views/openhospital_appointment_views.xml',
        'views/openhospital_lab_views.xml',
        'views/sale_order_views.xml',

    ],

    # only loaded in demonstration mode
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False
}
