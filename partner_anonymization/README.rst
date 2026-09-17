.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Partner anonymization
=====================

Allows anonymization partners.
Anonymize partner name with UUID string and deactivates the partner.

Deletes following info:

- Street
- Street specifier
- Email
- Title
- Phone
- Mobile
- Website

Country, City and Zip will NOT be deleted, as they are not identifiable
information. They can be used for reporting purposes.

If the ``mass_mailing_partner`` module is installed, any ``mailing.contact``
linked to the partner is removed as part of anonymization, before the
partner's own email is cleared. This order matters:
``mass_mailing_partner`` has its own constraint that forbids clearing a
partner's email while a mailing contact is still linked to it, so the link
has to go first.

Configuration
=============
\-

Usage
=====
\-

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@futural.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
