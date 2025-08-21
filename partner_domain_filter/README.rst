.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Partner domain filter
=====================

This module provides **Partner Domain Filters** that can be used
in the Website for conditional snippet visibility **and** in other modules.

It allows website snippets to be shown or hidden depending on whether
the logged-in user's partner record matches a domain expression.
At the same time, the filters are generic and reusable, so other modules
can reference them for partner-based logic.

Features
========

* Define reusable **partner domain filters** in the backend.
* Filters are simple Odoo domain expressions (e.g. ``[('country_id.code', '=', 'US')]``).
* Adds a **snippet option** ("Partner Domain") in Website Builder’s conditional visibility menu.
* Frontend widget evaluates filters and marks matching partner domains in the HTML dataset.
* Filters are **not limited to website use** — they can be applied in other modules for any partner-related logic.


Configuration
=============
1. Go to **Contacts > Configuration > Partner Filters**.
2. Create a new **Partner Domain Filter**:
   * Name = filter name
   * Filter Domain = Odoo domain expression, e.g.  
     ``[('is_company', '=', True)]``  
     or  
     ``[('country_id.code', '=', 'FI')]``

Usage
=====
**In Website Builder**:
* Edit any snippet and open the **Visibility Options**.
* Select **Partner Domain** from the conditional visibility menu.
* Choose one or more filters.  
  The snippet will only be shown to users whose partner matches at least one filter.

**In other modules**:
* The ``partner.domain.filter`` records can be referenced directly in Python or XML.
* For example, backend logic can check if a given partner matches a filter before
  applying discounts, granting access, or running scheduled actions.

**At runtime in Website**:
* When a user loads the page:
  - The widget calls the backend with the filter ID(s).
  - If a filter matches, its name is added to  
    ``<html data-partner-domain="FilterName">``.
  - CSS selectors or snippet conditions use this dataset
    to determine visibility.

How it works
============

1. **Model**:  
   ``partner.domain.filter``  
   Stores name, description, and domain expression.

2. **Controller**:  
   ``/website/partner_domain_check``  
   Checks if the current logged-in user's partner matches the domain filter.

3. **Widget (JS)**:  
   ``PartnerDomainChecker``  
   Reads the filter configuration from snippet attributes, calls the backend,
   and updates the ``<html>`` dataset with matching domain names
   (``data-partner-domain``).

4. **Snippet Option**:  
   Integrated into Website Builder under *Conditional Visibility*.  
   Allows editors to choose a partner domain filter from the UI
   and apply it to a snippet.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
