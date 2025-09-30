from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    partner_map_view_start_zoom = fields.Integer(
        string="Start zoom",
        store=True,
        config_parameter="partner_map_view.start_zoom",
        default=15
    )
    partner_map_view_start_latitude = fields.Float(
            string="Start latitude",
            store=True,
            config_parameter="partner_map_view.start_latitude",
            default=61.49911
    )
    partner_map_view_start_longitude = fields.Float(
            string="Start longitude",
            store=True,
            config_parameter="partner_map_view.start_longitude",
            default=23.78712
    )
