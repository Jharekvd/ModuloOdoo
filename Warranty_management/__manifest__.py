{
    'name': 'Warranty Management',
    'version': '1.0',
    'summary': 'Manage product warranties for sold items',
    'author': 'JhamiYoel',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/warranty_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}