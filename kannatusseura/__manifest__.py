# -*- coding: utf-8 -*-
{
    'name': "kannatusseura",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'application': False,
    'installable': True,
    'depends': ['contacts', 'kannatusseura_category'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}

