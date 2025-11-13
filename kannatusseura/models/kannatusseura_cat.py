from odoo import models, fields, api


class KannatusseuraCat(models.Model):
    _name = 'kannatusseura.cat'
    _rec_name = 'kannatusseura_cat_name'
    

    kannatusseura_cat_name = fields.Selection(
        selection=[
            ('hockey', 'Hockey'),
            ('soccer', 'Soccer'),
            ('formula1', 'Formula 1'),
        ],
        string="Kannatusseura cat",
        required=True
    )

    kannatusseura_cat_code = fields.Char(
        string="KanCatCode"
    )
