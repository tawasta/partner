##############################################################################
#
#    Author: Futural Oy
#    Copyright 2026- Futural Oy (https://futural.fi)
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
    "name": "Partner: Economic Development Centres",
    "summary": "Adds option to create economic development centres "
    "and links them to partners based on partner zip codes",
    "version": "17.0.1.0.0",
    "category": "CRM",
    "website": "https://github.com/tawasta/partner",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base_location_nuts_zip_code_mapping"],
    "data": [
        "security/ir.model.access.csv",
        "views/economic_development_centre_views.xml",
        "views/municipality_code_edc_code_mapping_views.xml",
        "views/res_partner.xml",
        "data/economic_development_centre_data.xml",
        "data/municipality_code_edc_code_mapping_data.xml",
    ],
    "demo": [],
}
