# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2014 - Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Partner Roles',
    'category': 'Sales',
    'version': '8.0.0.5.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['crm'],
    'description': "Adds tag-like roles for partners depending on if they are companies or contacts",
    'installable': True,
    'data': [
        'view/res_partner.xml',
        'security/ir.model.access.csv',
    ]
}