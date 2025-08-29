.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================================
Website Partner Domain Visibility
=================================
This module extends the Odoo Website Editor by allowing snippet visibility
to be controlled using **Partner Domain Filters** defined in the
`partner_domain_filter` module.

Features
========
* Adds a new *Conditional Visibility* option in Website Editor: **Partner Domain**.
* Uses backend-defined filters (`partner.domain.filter`) to decide whether
  snippets should be shown to the current user.
* Provides a JSON-RPC endpoint and a frontend widget to dynamically evaluate
  partner filters.
* Updates the `<html>` dataset (`data-partner-domain`) with the names of matched
  filters for the logged-in user.

Configuration
=============
1. Install and configure the dependency module **partner_domain_filter**.
2. Create one or more Partner Domain Filters from:
   *Contacts → Configuration → Partner Filters*
3. Each filter must have a valid Odoo domain expression based on `res.partner`.

Usage
=====
1. In Website Editor, select a snippet.
2. Open the *Conditional Visibility* panel.
3. Choose **Partner Domain** as the visibility option.
4. Select the filter(s) you want to apply.
5. The snippet will only be visible if the current user’s partner matches the filter domain.


How it works
============
* The backend controller `/website/partner_domain_check` evaluates whether
  the current user's partner record matches a given filter domain.
* The frontend widget `PartnerDomainChecker` sends JSON-RPC requests to the backend
  and updates the `<html>` element with matched filter names.
* The Website Editor uses this dataset to decide if a snippet should be rendered.

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
