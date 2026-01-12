import base64
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
    def is_valid_social_security_number(social_security_number: str) -> bool:
        pattern = r"^(\d{2})(0[1-9]|1[0-2])(\d{2})([-+A])(\d{3})([0-9A-Ya-y])$"
        match = re.match(pattern, (social_security_number or "").strip())
        if not match:
            return False

        day, month, year, century, individual, checksum = match.groups()
        number_to_check = f"{day}{month}{year}{individual}"
        modulo_31 = int(number_to_check) % 31
        checksum_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        return checksum.upper() == checksum_chars[modulo_31]

    # ---- Key handling ----

    def _get_encryption_key(self) -> bytes:
        parameter_name = "social_security_number_encryption_key"
        s = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(parameter_name, default="")
            .strip()
        )

        if not s:
            raise ValueError(
                _(
                    "The encryption key was not found or it is empty. "
                    "Please set system parameter '%s'."
                )
                % parameter_name
            )

        key = s.encode("utf-8")  # safe: your key is ASCII anyway
        return (key + b"\x00" * 32)[:32]

    # ---- Encrypt ----

    def _encrypt_social_security_number(self, social_security_number: str) -> bytes:
        """
        Payload format:
          base64( nonce(12 bytes) || tag(16 bytes) || ciphertext )
        AES-256-GCM, AAD = b"".
        """
        key = self._get_encryption_key()
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)

        ct_and_tag = aesgcm.encrypt(nonce, social_security_number.encode("utf-8"), b"")
        ciphertext = ct_and_tag[:-16]
        tag = ct_and_tag[-16:]

        payload = nonce + tag + ciphertext
        return base64.b64encode(payload)

    # ---- Decrypt ----

    def decrypt_social_security_number(self, encrypted_data_base64, input_key: str):
        """
        Decrypt payload format:
        base64( nonce(12) || tag(16) || ciphertext )
        AES-256-GCM, AAD = b"".
        """
        # Normalize input types from Odoo field (bytes / memoryview) and wizard (str)
        if isinstance(encrypted_data_base64, memoryview):
            encrypted_data_base64 = encrypted_data_base64.tobytes()
        if isinstance(encrypted_data_base64, str):
            encrypted_data_base64 = encrypted_data_base64.encode("utf-8")

        system_key = self._get_encryption_key()

        # Validate user-provided key equals system key
        input_s = (input_key or "").strip()
        if not input_s:
            _logger.error("User provided key is empty.")
            return _("The key you provided is incorrect.")

        input_key_bytes = (input_s.encode("utf-8") + b"\x00" * 32)[:32]
        if input_key_bytes != system_key:
            _logger.error("Provided key != system key.")
            return _("The key you provided is incorrect.")

        # Decode stored payload (standard base64)
        try:
            raw = base64.b64decode(encrypted_data_base64)
        except Exception as e:
            _logger.error("Stored encrypted data is not valid base64: %r", e)
            return _("Decryption failed")

        # Validate minimum (nonce+tag+ct>=1)
        if len(raw) < 12 + 16 + 1:
            _logger.error("Encrypted payload too short: %s bytes", len(raw))
            return _("Decryption failed")

        nonce = raw[:12]
        tag = raw[12:28]
        ciphertext = raw[28:]

        aesgcm = AESGCM(system_key)

        # Layout A: nonce || tag || ciphertext  (cryptography expects ciphertext||tag)
        try:
            pt = aesgcm.decrypt(nonce, ciphertext + tag, b"")
            return pt.decode("utf-8")
        except Exception as e:
            _logger.error("AESGCM decrypt failed (layout A nonce||tag||ct): %r", e)

        # Fallback layout B: nonce || ciphertext || tag
        try:
            nonce_b = raw[:12]
            ciphertext_b = raw[12:-16]
            tag_b = raw[-16:]
            pt = aesgcm.decrypt(nonce_b, ciphertext_b + tag_b, b"")
            _logger.error(
                "AESGCM decrypt succeeded with fallback layout B (nonce||ct||tag)"
            )
            return pt.decode("utf-8")
        except Exception as e:
            _logger.error("AESGCM decrypt failed (layout B nonce||ct||tag): %r", e)
            return _("Decryption failed")

    # ---- ORM hooks ----

    @api.model
    def create(self, vals):
        ssn = (vals.get("social_security_number") or "").strip()
        if ssn:
            if not self.is_valid_social_security_number(ssn):
                raise exceptions.ValidationError(
                    _("The format of the personal identification number is not valid.")
                )
            vals[
                "encrypted_social_security_number"
            ] = self._encrypt_social_security_number(ssn)
            vals["ssn_hash"] = hashlib.sha256(ssn.encode("utf-8")).hexdigest()
            vals.pop("social_security_number", None)
        return super().create(vals)

    def write(self, vals):
        ssn = (vals.get("social_security_number") or "").strip()
        if ssn:
            if not self.is_valid_social_security_number(ssn):
                raise exceptions.ValidationError(
                    _("The format of the personal identification number is not valid.")
                )
            vals[
                "encrypted_social_security_number"
            ] = self._encrypt_social_security_number(ssn)
            vals["ssn_hash"] = hashlib.sha256(ssn.encode("utf-8")).hexdigest()
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
