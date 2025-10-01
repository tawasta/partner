from odoo import fields, models


class View(models.Model):
    """
    Extends the base "ir.ui.view" model to include a new type of view
    called "Partner Map".
    """

    _inherit = "ir.ui.view"
    type = fields.Selection(selection_add=[("partnerMapView", "Partner Map")])


class IrActionsActWindowView(models.Model):
    """
    Extends the base "ir.actions.act_window.view" model to include
    a new view mode called "Partner Map".
    """

    _inherit = "ir.actions.act_window.view"
    view_mode = fields.Selection(
        selection_add=[("partnerMapView", "Partner Map")],
        ondelete={"partnerMapView": "cascade"},
    )
