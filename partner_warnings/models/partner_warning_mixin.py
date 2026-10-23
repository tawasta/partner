from odoo import api, models
from odoo.exceptions import ValidationError

# Selection values for the warning level fields defined by the modules that
# use the mixin
WARNING_LEVELS = [
    ("warning", "Warning"),
    ("popup_warning", "Popup Warning"),
    ("blocking_warning", "Blocking Warning"),
]


class PartnerWarningMixin(models.AbstractModel):
    """Popup and blocking warnings from the partner of a document.

    Inherit this in a model that has a ``partner_id`` field and set the
    names of the res.partner fields that hold the warning message and the
    warning level.
    """

    _name = "partner.warning.mixin"
    _description = "Partner Warning Mixin"

    def __init__(self, *args, **kwargs):
        _warning_message_field = None
        _warning_level_field = None
        super().__init__(*args, **kwargs)

    @api.onchange("partner_id")
    def _onchange_partner_id_popup_warning(self):
        partner = self.partner_id
        if not partner:
            return
        message = partner[self._warning_message_field]
        if message and partner[self._warning_level_field] == "popup_warning":
            return {
                "warning": {
                    "title": self.env._("Warning from customer!"),
                    "message": message,
                }
            }

    def write(self, vals):
        if vals.get("partner_id"):
            self._check_blocking_warning(vals["partner_id"])
        return super().write(vals)

    @api.model
    def _check_blocking_warning(self, partner_id):
        partner = self.env["res.partner"].browse(partner_id)
        if partner[self._warning_level_field] != "blocking_warning":
            return
        error = self.env._(
            "Blocked: customer has a blocking warning to prevent saving!"
        )
        message = partner[self._warning_message_field]
        if message:
            error = f"{error}\n{partner.display_name} - {message}"
        raise ValidationError(error)
