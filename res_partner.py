from openerp.osv import osv, fields
from openerp.tools.translate import _

class ResPartner(osv.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    _columns = {
        'customer_of': fields.many2many(
            'res.company',
            'res_company_customer_rel'
            '',
            'id',
            string=_('Customer of')
        ),
        'supplier_of': fields.many2many(
            'res.company',
            'res_company_supplier_rel'
            '',
            'id',
            string=_('Supplier of')
        ),
    }
    
ResPartner()