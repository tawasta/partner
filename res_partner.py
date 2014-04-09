from openerp.osv import osv, fields
from openerp.tools.translate import _

class ResPartner(osv.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    def _get_selection(self, cursor, user_id, context=None):
        return (
            ('allowed', _('Allowed')),
            ('ask', _('Confirm by case')),
            ('no', _('Not allowed'))
        )

    _columns = {
        'referenceright': fields.selection( _get_selection, 'Reference right' )
    }
    
    _defaults = {
        'referenceright': False,             
    }
    
ResPartner()