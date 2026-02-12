.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================
Role Auto IR Filters
====================
This module automatically creates and maintains ``ir.filters`` records
based on user roles defined using the ``base_user_role`` module.

When a role is assigned, updated, or removed through
``res.users.role.line``:

* Filters are automatically created or updated for the user
* Domains can dynamically include the user's companies
* Filters are deactivated if the role is no longer active
* Role validity dates are respected

This allows centralized management of default filters per role
without manual configuration for each user.

Configuration
=============
#. Go to:

   **Settings → Administration → Role Auto Filters**

#. Create a rule and define:

   * The role that triggers the filter
   * Target model for the filter
   * Filter name
   * Optional action restriction
   * Domain template (Python domain expression)
   * Whether only leaf companies (companies without children)
     should be included

The domain template can use the variable::

    user_company_ids

which contains the applicable company IDs for the user.

Usage
=====
Assign or modify user roles normally using the user role functionality.

Filters will automatically:

* Be created when a role is assigned
* Update when role validity changes
* Be disabled when the role is removed or expires

No manual filter maintenance is required.

Known issues / Roadmap
======================
* Filters are updated when roles change, but not automatically when
  user company assignments change.
* Future improvements may include optional updates on company changes
  and additional rule configuration flexibility.

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
