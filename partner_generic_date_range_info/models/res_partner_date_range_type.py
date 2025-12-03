from odoo import _, fields, models
from odoo.exceptions import UserError


class ResPartnerDateRangeType(models.Model):
    _name = "res.partner.date.range.type"
    _description = "Partner Date Range Information Type"

    name = fields.Char(required=True)

    active = fields.Boolean(default=True)

    code = fields.Char(
        help="Technical helper field that can be set if you need to access "
        "date ranges of this type programmatically for e.g. calculations.",
        groups="base.group_no_one",
    )
    notes = fields.Text(string="Internal Notes")

    def write(self, vals):
        """
        Prevent changing the code field via UI afterwards.
        """
        if "code" in vals:
            for rec in self:
                if rec.code and vals.get("code") != rec.code:
                    raise UserError(
                        _("The code field cannot be changed after creation.")
                    )
        return super().write(vals)
