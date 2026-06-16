##############################################################################
#
#    Author: Futural Oy
#    Copyright 2025- Futural Oy (https://futural.fi)
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
    "name": "Kannatusseura", 
    "version": "17.0.1.0.0", 
    "category": "Project",
    "summary": "Adds support club to the odoo contacts",
    "website": "",
    "author": "Futural",
    "licence": "AGPL-3",
    "application": False, 
    "installable": True, 
    "depends": [
        "contacts",
        "base",
        "portal",
        "website",
        ],
    "data": [
        "views/kannatusseura_kategoria.xml",
        "views/res_partner_views.xml",
        "data/ir_cron_data.xml",
        "security/ir.model.access.csv",
        "views/portal_my_account_extend.xml",
        ], 
} 
