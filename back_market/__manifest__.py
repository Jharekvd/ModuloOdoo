{
    'name': 'BackMarket',
    'version': '1.0',
    'summary': 'Reducción de precios para objetos devueltos',
    'author': 'Jhamil Yoel',
    'category': 'Sales',
    'depends': ['base', 'sale', 'stock','product'],  # Verifica que el módulo 'stock' es necesario.
    'data': [
        'security/ir.model.access.csv', 
        'views/backmarket_view.xml',
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3'
}


