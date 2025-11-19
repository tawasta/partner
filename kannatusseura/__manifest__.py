# -*- coding: utf-8 -*-
{
    'name': "kannatusseura",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/kannatusseura_views.xml',
        'views/kannatusseura_cat.xml',
        'views/res_partner_views.xml',

    ],
    'demo': [
        'demo/demo.xml',
    ],
}

