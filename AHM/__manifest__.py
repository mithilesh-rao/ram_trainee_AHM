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
        'views/AHM_view.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}