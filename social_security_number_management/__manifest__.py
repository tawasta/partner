##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2023 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    "name": "Partner: Social Security Number Management",
    "summary": "Store SSN for partners in an encrypted format",
    "version": "17.0.1.0.0",
    "category": "Specific Industry Applications",
    "website": "https://github.com/tawasta/odoo/partner",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["base", "contacts"],
    "external_dependencies": {
        "python": ["cryptography.hazmat.primitives.ciphers.aead"]
    },
    "data": [
        "data/config_parameter.xml",
        "security/rule.xml",
        "security/ir.model.access.csv",
        "views/partner.xml",
        "wizards/decrypt_wizard_views.xml",
    ],
}
