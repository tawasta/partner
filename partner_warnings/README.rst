.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================
Partner Warnings
================

Generic popup and blocking warnings from the partner of a document. The
module has no user interface of its own: other modules use it to add the
behavior to their documents.

* Popup Warning

  * Show a popup when the partner is chosen on the document, if the partner
    has a warning message

* Blocking Warning

  * Prevent changing the partner of an existing document to a partner that
    has a blocking warning

Configuration
=============
\-

Usage
=====

* Developer

  * Depend on this module and inherit the abstract model
    ``partner.warning.mixin`` in the model that has a ``partner_id`` field

    * Set ``_warning_message_field`` to the name of the res.partner field
      holding the warning message
    * Set ``_warning_level_field`` to the name of the res.partner field
      holding the warning level
    * Use ``WARNING_LEVELS`` (partner_warnings.models.partner_warning_mixin)
      as the selection of the level field

  * Add the level field to the partner form

Modules using this module

* sale_warnings
* stock_warnings

Known issues / Roadmap
======================

* The blocking warning is checked only when the partner of an existing
  document is changed, not when a document is created.

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
