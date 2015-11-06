# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jarmo Kortetjärvi
#    Copyright 2015 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################
{
    'name': 'Partner Reference Right',
    'category': 'Sales',
    'version': '8.0.0.2.2',
    'author': '''
Vizucom Oy,
Oy Tawasta OS Technologies Ltd.
''',
    'license': 'AGPL-3',
    'depends': [],
    'installable': True,
    'data': [
         'data/reference_rights.xml',
         'view/res_partner.xml',
         'view/reference_right.xml',
         #'security/refright_security.xml',
         'security/ir.model.access.csv',
     ]
}
