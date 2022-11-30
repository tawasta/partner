.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============================================
Determine Partner's Fiscal Position by region
=============================================

When creating a partner, its selected country determines the fiscal position
for that partner. This works with multi-companies also, because all the
companies are looped through and a fiscal position is assigned within
context of that company's partner's country. So a country can be domestic
for one company but belong to EU for another company, for example.

All the companies are looped through. These conditions are checked with each
company:

* If the selected country matches with a country of a company's partner,
  then a fiscal position is set whose Type is 'Domestic'.

* If the selected country is in Europe, a fiscal position is set whose
  Type is 'EU'.

* If the selected country is outside of Europe, a fiscal position is
  set whose Type is 'non-EU'.

This means that different fiscal positions can be assigned for all the companies
for the created partner.

Configuration
=============
* No special configuration is needed

Usage
=====
* Go to Apps and install this module

Known issues / Roadmap
======================
* Multi-companies are not necessary

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
