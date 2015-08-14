from openerp.osv import osv, fields
from openerp.tools.translate import _

class SaleOrder(osv.Model):
    _inherit = "sale.order"
    
    # When quotation is about to be set to "In finalization"

    def action_in_finalization(self, cr, uid, ids, context=None):
        # Update the "customer of" field
        sale_order = self.browse(cr, uid, ids, context)[0]
        res_partner = self.pool.get('res.partner')
        
        res_partner.write(cr, uid, sale_order.partner_id.id, {'customer_of': [(4, sale_order.company_id.id)]}, context=context)
        
        res = super(SaleOrder, self).action_in_finalization(cr, uid, ids, context)

        return res
