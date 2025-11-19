from odoo import models, fields, api # type: ignore
from odoo.exceptions import ValidationError # type: ignore

class KannatusseuraModel(models.Model):
    _name = 'kannatusseura.model'
    _description = 'Kannatusseura Model'

    _sql_constraints = [
                            ('unique_code_unique', 'unique(unique_code)', 'Code already in use, try a different one.')
                        ]       
    

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

    kannatusseura_kategoria = fields.Many2one("kannatusseura.cat", string="Kannatusseura kategoria")

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
    
    @api.constrains('kannatusseura_code')
    def _check_unique_code(self):
        for record in self:
            if record.kannatusseura_code:
                existing = self.search([
                    ('kannatusseura_code', '=', record.kannatusseura_code),
                    ('id', '!=', record.id)
                ], limit=1)
                if existing:
                    raise ValidationError("This code is already assigned to another contact.")




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

