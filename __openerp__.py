# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015 - Oy Tawasta Technologies Ltd. (http://www.tawasta.fi)
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
    'name': 'Partner Internal Note Extension',
    'category': 'CRM',
    'version': '0.3',
    'author': 'Oy Tawasta Technologies Ltd.',
    'website': 'http://www.tawasta.fi',
    'depends': ['crm'],
    'description': '''
* Allows multiple internal notes with note titles and creator and editor information.
''',
    'data': [
         'view/res_partner.xml',
         'view/partner_note.xml',
         'security/ir.model.access.csv',
     ]
}
