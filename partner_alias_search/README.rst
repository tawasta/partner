.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================
Contact Alias Search
====================

This module adds support for alternative names (aliases) for contacts.

Aliases can be used when searching contacts from Many2one fields and are
especially useful when external systems use different names for the same
legal entity.

Configuration
=============
No additional configuration is required.

Usage
=====
* Open a contact.
* Navigate to the **Aliases** tab.
* Add one or more alternative names.

When contacts are merged using the standard Odoo merge wizard,
the names of the merged contacts are automatically stored as aliases
for the surviving contact.

This allows imported or external data to continue matching the correct
contact even after company renames or contact consolidation.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
