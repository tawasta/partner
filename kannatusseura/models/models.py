# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore
import logging
import xmlrpc.client


class ResPartner(models.Model):
    _inherit = 'res.partner'

    _logger = logging.getLogger(__name__)
    

    kannatusseura_name = fields.Selection(
        string="Kannatusseura Name",
        selection=[
            ('hifk', 'HIFK'),
            ('tappara', 'Tappara'),
            ('ilves', 'Ilves'),
            ('lukko', 'Lukko'),
            ('kärpät', 'Kärpät'),
            ('kalpa', 'KalPa'),
            ('jyp', 'JYP'),
            ('pelicans', 'Pelicans'),
            ('sport', 'Sport'),
            ('kookoo', 'KooKoo'),
            ('redbull', 'Red Bull Racing'),
            ('mclaren', 'McLaren'),
            ('astonmartin', 'Aston Martin'),
            ('alpine', 'Alpine'),
            ('williams', 'Williams'),
            ('haas', 'Haas'),
            ('sauber', 'Sauber'),
            ('alphatauri', 'AlphaTauri'),
            ('barcelona', 'FC Barcelona'),
            ('realmadrid', 'Real Madrid'),
            ('manutd', 'Manchester United'),
            ('mancty', 'Manchester City'),
            ('liverpool', 'Liverpool'),
            ('bayern', 'Bayern Munich'),
            ('psg', 'Paris Saint-Germain'),
            ('hjk', 'HJK Helsinki'),
            ('kups', 'KuPS'),
            ('interturku', 'FC Inter Turku'),
        ],
    )

    kannatusseura_code = fields.Char(
        string="Kannatusseura Code"
    )

    kannatusseura_kategoria = fields.Many2one("kannatusseura.cat", string="Kannatusseura cat")

    #uutta

    # url = "http://localhost:8069/"
    # db = "db"
    # username = 'admin'
    # password = 'admin'

    # uid = common.authenticate(db, username, password, {})

    # models.execute_kw(db, None, password, 'res.partner', 'search', [[['kannatusseura_code', '=', True]]])
    
    #/uutta

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|',
                      ('name', operator, name),
                      ('kannatusseura_name.name', operator, name),
                      ('kannatusseura_code', operator, name)]
        partners = self.search(domain + args, limit=limit)
        return partners.name_get()



    # !!!!!  EI TOIMI KOSKA DYNAAMINEN DROPDOWN EI ILMEISESTI KOVIN MAHDOLLINEN ODOOSSA
    # @api.onchange('kannatusseura_kategoria')
    # def _onchange_kannatusseura_kategoria(self):
        

    #     # if not self.kannatusseura_kategoria:
    #     #     self.kannatusseura_name = None
    #     #     return

    #     category = self.kannatusseura_kategoria.kannatusseura_cat_name
        
    #     logging.getLogger(__name__).info(category)

    #     selections = {
    #         'hockey': [
    #             ('hifk', 'HIFK'),
    #             ('tappara', 'Tappara'),
    #             ('ilves', 'Ilves'),
    #             ('lukko', 'Lukko'),
    #             ('kärpät', 'Kärpät'),
    #             ('kalpa', 'KalPa'),
    #             ('jyp', 'JYP'),
    #             ('pelicans', 'Pelicans'),
    #             ('sport', 'Sport'),
    #             ('kookoo', 'KooKoo'),
    #         ],
    #         'formula1': [
    #             ('redbull', 'Red Bull Racing'),
    #             ('mclaren', 'McLaren'),
    #             ('astonmartin', 'Aston Martin'),
    #             ('alpine', 'Alpine'),
    #             ('williams', 'Williams'),
    #             ('haas', 'Haas'),
    #             ('sauber', 'Sauber'),
    #             ('alphatauri', 'AlphaTauri'),
    #         ],
    #         'soccer': [
    #             ('barcelona', 'FC Barcelona'),
    #             ('realmadrid', 'Real Madrid'),
    #             ('manutd', 'Manchester United'),
    #             ('mancty', 'Manchester City'),
    #             ('liverpool', 'Liverpool'),
    #             ('bayern', 'Bayern Munich'),
    #             ('psg', 'Paris Saint-Germain'),
    #             ('hjk', 'HJK Helsinki'),
    #             ('kups', 'KuPS'),
    #             ('interturku', 'FC Inter Turku'),
    #         ],
    #     }
    #     logging.getLogger(__name__).info(selections[category])
    #     # allowed = selections.get(category, [])
    #     # self.kannatusseura_name = None
            
    #     return {
    #         'domain': {
    #             'kannatusseura_name': selections[category],
    #         }
    #     }




