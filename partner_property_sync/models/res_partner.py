from odoo import fields, models


class ResPartnerAnalysis(models.Model):

    _name = "res.partner.analysis"

    _inherits = {"res.partner": "partner_id"}

    comment = fields.Text(string="Internal note")
