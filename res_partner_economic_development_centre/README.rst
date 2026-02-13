.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================================
Partner: Economic Development Centres
=====================================

* Adds option to create economic development centres (elinvoimakeskukset
  in Finnis) and link them to partners
* Utilizes the mappings of base_location_nuts_zip_code_mapping to automatically
  set the centre for a partner when their zip code or country changes.
* Creates the 10 Finnish economic development centres (as of start of 2026)
  when module installs, and creates a mapping table of how the EDC codes
  map to Finnish municipality codes (as of start of 2026)  

Configuration
=============
* None needed

Usage
=====
* New field is shown in partner form view
* Economic development centres can be managed in Contacts -> Settings

Known issues / Roadmap
======================
* Pull municipality code -  development centres mapping data periodically from
  https://stat.fi/fi/luokitukset/corrmaps/kunta_1_20260101%23evk_1_20260101 ,
* Currently the mappings tables are just "dumb" code pair tables, could consider
  setting up actual relations for more convenient lookups, but that will 
  require managing e.g. municipalities as Odoo records instead.
  
Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
