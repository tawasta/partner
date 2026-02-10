from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    geographic_region_id = fields.Many2one(
        comodel_name="geographic.region", string="Geographic Region"
    )
