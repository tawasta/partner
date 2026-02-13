import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MunicipalityCodeEdcCodeMapping(models.Model):
    _name = "res.municipalicy_code_edc_code_mapping"
    _description = "Municipality Code to Economic Development Centre code mapping"

    # Mapping data is provided by stat.fi but updates are not currently being
    # checked for automatically.
    # https://stat.fi/fi/luokitukset/corrmaps/kunta_1_20260101%23evk_1_20260101

    municipality_code = fields.Char(required=True)
    economic_development_centre_code = fields.Char(required=True)
