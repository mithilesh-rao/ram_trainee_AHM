{
    'name': "AHM",
    'version': '1.0',
    'depends': ['base','website'],
    'author': "Animal Health Monitorig",
    'category': 'Category',
    'description': """
    name 
    """,
    
    'data': [
        'security/ir.model.access.csv',

        'reports/reports.xml',
        'views/AHM_view.xml',
        'views/patient_detail_view.xml',
        
        'views/staff_management_view.xml',
        'views/cost_management_view.xml',
        'views/inventory_view.xml',
        'views/templates.xml',
        
        'wizard/wizard_view.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}