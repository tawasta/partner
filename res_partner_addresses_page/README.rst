.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
:target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================
Split partner addresses to separate pages
=========================================

Split partner (company) addresses to separate pages.

By default "Contacts & Addresses" is one page.
This module will split them to "Contacts" and "Addresses"

The default view will be tree instead of kanban
The "main company only"-default filter is removed.

Simplifies partner type/company_type logic down to five variants (type, company_type):

* (Parent) Company (contact, company)
* Contact (contact, person)
* Invoice (invoice, person)
* Delivery (delivery, person)
* (Child) Company (other, company)


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

* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
:alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
