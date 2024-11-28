##############################################################################
#
#    Author: Futural Oy
#    Copyright 2021 Futural Oy (https://futural.fi)
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
    "name": "Audit Log Rules - Partner",
    "summary": "Adds audit log rules for res partner",
    "author": "Futural",
    "license": "AGPL-3",
    "website": "https://github.com/tawasta/partner",
    "category": "Logging",
    "application": False,
    "installable": True,
    "version": "17.0.1.0.0",
    "depends": ["contacts", "auditlog"],
    "data": ["data/rules.xml"],
    "demo": [],
}
