.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

==========================================
Partner: Social Security Number Management
==========================================
This module adds secure handling of Finnish personal identification numbers (social
security numbers) to partners.

The personal identification number is **never stored in plain text** in the database.
Instead, it is:

* validated using the official Finnish format and checksum rules
* encrypted using AES-GCM encryption
* stored only as encrypted binary data
* additionally indexed using a SHA256 hash to ensure uniqueness

Viewing the personal identification number requires a dedicated security group and
a correct decryption key.

Installation
============

1. Install the module as any Odoo addon.
2. Ensure dependency ``cryptography`` is installed on the server:
   ::

      pip install cryptography

Configuration
=============
Generate a secure encryption key:

::

   openssl rand -base64 32

Then configure it in Odoo:

* Go to:
  ``Settings → Technical → Parameters → System Parameters``
* Create system parameter:

  * Key:
    ``social_security_number_encryption_key``
  * Value:
    (your generated base64 key)

Usage
=====
1. Open a partner form.
2. Enter Finnish Personal Identification Number into "Personal Identification Number".
3. Save the form.
4. The value is immediately encrypted.

To view the value:

1. Click **Show Personal ID** button.
2. Enter the decryption key.
3. The decrypted value appears in a temporary notification.


Known issues / Roadmap
======================
\-

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
