{
    'name': "Animal Health Monitoring",
    'version': '1.0',
    'depends': ['base','web_dashboard', 'portal'],
    'author': "Animal Health Monitorig",
    'category': 'Category',
    'description': """
    name 
    """,
    
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/data.xml',

        'reports/reports.xml',
        'views/AHM_view.xml',
        'views/patient_detail_view.xml',
        
        'views/staff_management_view.xml',
        'views/cost_management_view.xml',
        'views/inventory_view.xml',
        'views/userregistration_view.xml',
        'views/homepage_view.xml',
        # 'views/template.xml',
        # 'views/templates.xml',
        
        # 'wizard/wizard_view.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}