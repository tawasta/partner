.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================
Partner: Generic Date Range Info Field
======================================

* Enables logging info about user-defineable start/end dates 
  for partners, e.g. their
  
  * join dates
  * perk eligibility dates
  * date-specific positions, e.g. board membership

Configuration
=============
* Configure the date range types in Contacts -> Settings
  -> Partner Date Range Based Information Types
* Each type also can be given a fixed "code" string, if the 
  related records will be used for calculations in other
  modules. The code cannot be changed in the UI afterwards.

Usage
=====
* Open partner form to see the new notebook tab
* If you are utilizing the "code" string for calculations, 
  the module contains some helper functions for this.
  See res_partner.py and use if needed.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
