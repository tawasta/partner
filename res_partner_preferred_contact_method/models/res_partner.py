from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    preferred_contact_method=fields.Many2one(
        comodel_name='res.contact_method',
        string="Preferred contact method",
        help="Preferred contact method",
    )
