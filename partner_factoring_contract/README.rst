.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================
Partner Factoring Contract
==========================

A generic, e-invoicing-operator-independent factoring contract on
partners and invoices. Stores the factoring agreement identifier and
type code, and lets other modules (e-invoicing formats, connectors)
map them into their own output without depending on each other.

Features
========

* **Factoring Contract** (Invoicing > Configuration > Factoring
  Contracts): name, agreement identifier, type code, and the bank
  account factoring payments are collected to.
* **Partner default**: a partner can have a default factoring
  contract (Contact form > Sales & Purchase tab).
* **Invoice**: an invoice picks up its partner's default factoring
  contract automatically when created, and can be overridden manually
  while still a draft (Invoice form > Other Info tab).

Configuration
=============
\-

Usage
=====

* Create a Factoring Contract under Invoicing > Configuration >
  Factoring Contracts.
* Set it as the default on the customer's Contact form, or on an
  individual draft invoice.

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
