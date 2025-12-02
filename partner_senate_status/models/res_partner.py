from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    senate_member = fields.Selection(
        selection=[
            ('no', 'No'),
            ('yes', 'Yes'),
        ],
        string='Senate Member',
        default='no',
        help='Is this partner a member of the senate?',
    )
