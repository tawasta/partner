from openerp.osv import osv, fields
from openerp.tools.translate import _
import logging
_logger = logging.getLogger(__name__)

class ResPartner(osv.Model):
    _inherit = "res.partner"
    
    def onchange_referenceright(self, cr, uid, ids, refrights, context=None):
        pass
    
    _columns = {
        'referenceright': fields.many2many(
            'res.partner.reference_right',
            'res_partner_reference_right_rel'
            '',
            'id',
            string=_('Reference right'),
        ),    
    }
    
    _defaults = {
        'referenceright': False,             
    }
