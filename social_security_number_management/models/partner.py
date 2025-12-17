import base64
import binascii
import hashlib
import logging
import os
import re

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from odoo import _, api, exceptions, fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    _sql_constraints = [
        (
            "ssn_hash_uniq",
            "unique(ssn_hash)",
            _("Personal identification number must be unique per partner."),
        ),
    ]

    social_security_number = fields.Char(
        string="Personal Identification Number",
        help="Finnish personal identity code. Will be encrypted on save.",
    )

    encrypted_social_security_number = fields.Binary(
        "Encrypted Personal Identification Number",
        invisible=True,
        readonly=True,
    )

    ssn_hash = fields.Char("SSN Hash", readonly=True, index=True)

    @api.constrains("social_security_number")
    def _check_social_security_number(self):
        for record in self:
            ssn = (record.social_security_number or "").strip()
            if ssn and not self.is_valid_social_security_number(ssn):
                raise exceptions.ValidationError(
                    _("The format of the personal identification number is not valid.")
                )

    @staticmethod
    def is_valid_social_security_number(social_security_number):
        pattern = r"^(\d{2})(0[1-9]|1[0-2])(\d{2})([-+A])(\d{3})([0-9A-Ya-y])$"
        match = re.match(pattern, social_security_number)
        if not match:
            return False

        day, month, year, century, individual, checksum = match.groups()
        number_to_check = f"{day}{month}{year}{individual}"
        modulo_31 = int(number_to_check) % 31
        checksum_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        return checksum.upper() == checksum_chars[modulo_31]

    def _get_encryption_key(self) -> bytes:
        """
        System parameter must be base64 of 32 bytes (AES-256 key).
        """
        parameter_name = "social_security_number_encryption_key"
        encoded_key = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(parameter_name, default="")
            .strip()
        )

        if not encoded_key:
            raise ValueError(
                _(
                    "The encryption key was not found or it is empty. "
                    "Please set system parameter '%s'."
                )
                % parameter_name
            )

        if len(encoded_key) % 4 != 0:
            raise ValueError(
                _("The length of the encryption key is not a multiple of four.")
            )

        try:
            key = base64.b64decode(encoded_key)
        except binascii.Error as e:
            _logger.error("Error decoding the encryption key: %s", e)
            raise ValueError(_("Decoding of the encryption key failed.")) from e

        if len(key) != 32:
            raise ValueError(
                _("Invalid encryption key length: expected 32 bytes, got %s.")
                % len(key)
            )
        return key

    def _encrypt_social_security_number(self, social_security_number: str) -> bytes:
        """
        Moodle/Odoo agreed payload format:
          base64( nonce(12 bytes) + tag(16 bytes) + ciphertext(11 bytes) )
        AES-256-GCM, AAD = b"".
        """
        key = self._get_encryption_key()
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)

        # cryptography returns ciphertext||tag (tag last)
        ct_and_tag = aesgcm.encrypt(nonce, social_security_number.encode("utf-8"), b"")
        ciphertext = ct_and_tag[:-16]
        tag = ct_and_tag[-16:]

        payload = nonce + tag + ciphertext
        return base64.b64encode(payload)

    def decrypt_social_security_number(self, encrypted_data_base64, input_key):
        """
        Decrypt payload in format:
          base64( nonce(12) + tag(16) + ciphertext(11) )
        AES-256-GCM, AAD = b"".
        """
        # Normalize input types
        if isinstance(encrypted_data_base64, memoryview):
            encrypted_data_base64 = encrypted_data_base64.tobytes()
        if isinstance(encrypted_data_base64, str):
            encrypted_data_base64 = encrypted_data_base64.encode()

        system_key = self._get_encryption_key()

        # Validate user-provided key equals system key
        try:
            input_key_bytes = base64.b64decode((input_key or "").strip())
        except Exception:
            _logger.error("User provided decryption key is not valid base64.")
            return _("The key you provided is incorrect.")

        if input_key_bytes != system_key:
            _logger.error("The key you provided does not match the system-defined key.")
            return _("The key you provided is incorrect.")

        # Decode stored payload
        try:
            raw = base64.b64decode(encrypted_data_base64)
        except Exception as e:
            _logger.error("Stored encrypted data is not valid base64: %r", e)
            return _("Decryption failed")

        # Speksi: 12 + 16 + 11 = 39
        if len(raw) != 39:
            _logger.error("Invalid encrypted payload length: expected 39, got %s", len(raw))
            return _("Decryption failed")

        nonce = raw[:12]
        tag = raw[12:28]
        ciphertext = raw[28:]  # 11 bytes

        aesgcm = AESGCM(system_key)
        try:
            # cryptography expects ciphertext||tag
            pt = aesgcm.decrypt(nonce, ciphertext + tag, b"")
            return pt.decode("utf-8")
        except Exception as e:
            _logger.error("AESGCM decrypt failed: %r", e)
            return _("Decryption failed")

    @api.model
    def create(self, vals):
        ssn = (vals.get("social_security_number") or "").strip()
        if ssn:
            if not self.is_valid_social_security_number(ssn):
                raise exceptions.ValidationError(
                    _("The format of the personal identification number is not valid.")
                )

            vals["encrypted_social_security_number"] = self._encrypt_social_security_number(ssn)
            vals["ssn_hash"] = hashlib.sha256(ssn.encode()).hexdigest()
            vals.pop("social_security_number", None)

        return super().create(vals)

    def write(self, vals):
        ssn = (vals.get("social_security_number") or "").strip()
        if ssn:
            if not self.is_valid_social_security_number(ssn):
                raise exceptions.ValidationError(
                    _("The format of the personal identification number is not valid.")
                )

            vals["encrypted_social_security_number"] = self._encrypt_social_security_number(ssn)
            vals["ssn_hash"] = hashlib.sha256(ssn.encode()).hexdigest()
            vals.pop("social_security_number", None)

        return super().write(vals)

    def action_decrypt_social_security_number(self):
        self.ensure_one()
        return {
            "name": _("Decrypt Personal ID"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "partner.ssn.decrypt.wizard",
            "target": "new",
            "context": {"default_partner_id": self.id},
        }

