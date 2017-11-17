{
    'name': "GNC_training",

    'summary': """Tamamen test amacli olusturulmus bir module""",

    'description': """
        GNC module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "emreozcan3320",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'installable': True,
    'auto_install': False,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
