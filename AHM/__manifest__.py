{
    'name': "AHM",
    'version': '1.0',
    'depends': ['base'],
    'author': "Animal Health Monitorig",
    'category': 'Category',
    'description': """
    name image contact email address specialization degree_certificate
    """,
    
    'data': [
        'security/ir.model.access.csv',

        'wizard/wizard_view.xml',
        'reports/reports.xml',

        'views/AHM_view.xml',
        'views/patient_detail_view.xml',
        'views/staff_management_view.xml',
        'views/cost_management_view.xml',
        'views/inventory_view.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}