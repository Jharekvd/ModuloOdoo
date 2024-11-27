# -*- coding: utf-8 -*-
{
    'name': "instalacion De Paquetes de Sofware",
    'author': "Jhamil Yoel",
    'description': "Modulo que gestiona la instalacion de paqetes",
    'category': 'Uncategorized',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base','product'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/software_package.xml',
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3'
}

