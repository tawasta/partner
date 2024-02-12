.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================
Simplify partner address management
===================================

Show company addresses and contacts in list instead of cards

Split partner address types to own fields: contacts and addresses

The default view will be tree instead of kanban.
Common address information can be modified in tree view
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
* Miika Nissi <miika.nissi@tawasta.fi>
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: https://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: https://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
