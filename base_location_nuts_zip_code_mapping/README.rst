.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================================================
NUTS Regions: zip code mappings + Finnish postcode importer
===========================================================

* Map country zip codes to NUTS items, enabling automatic NUTS level selections for contacts. 
* Support for importing Finnish postcode from Posti data

  * Also municipality names and codes (kuntanumerot, e.g. 837 for Tampere) get imported as well
    as additional info although they are not required by the mappings to work.

* For NUTS level info regarding Finland, see

  * https://stat.fi/fi/luokitukset/nuts/nuts_2_20260101


Configuration
=============
* You should have the OCA base_location_nuts module installed and its own importer already 
  run.
* Mappings can be managed via Contacts - Settings - ZIP Code NUTS item mappings
* In Finland you'll likely want to also run Contacts - Settings - Import Posti Zip Codes  

  * Importer takes in a DAT file provided by Posti at https://www.posti.fi/webpcode/ and 
    populates mappings from it. 

Usage
=====
* After mappings are in place, change a partner's postcode or country. If a suitable 
  mapping is found, the four NUTS levels are populated automatically for the partner.

Known issues / Roadmap
======================
* Future feature: consider scraping https://www.posti.fi/webpcode
  periodically for the most recent PCF .dat file and autoimport it.

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
