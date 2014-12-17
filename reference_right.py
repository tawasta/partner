from openerp.osv import osv, fields
from openerp import SUPERUSER_ID
from openerp.tools.translate import _
import logging
_logger = logging.getLogger(__name__)

class Reference_right(osv.Model):
    _name = "res.partner.reference_right"
    _order = "company_id, code"
    
    ''' When module is installed, fetch all companies and create reference rights '''
    def _init_reference_rights(self, cr, uid, ids=None, context=None):
        ref_rights = {
            'reference_right_allowed': _('Allowed'),
            'reference_right_ask': _('Ask'),
            'reference_right_no': _('No Right'),
        }

        company_obj = self.pool.get('res.company')
        refright_obj = self.pool.get('res.partner.reference_right')
        
        company_ids = company_obj.search(cr, SUPERUSER_ID, [],order='id')
        
        for company in company_obj.browse(cr, SUPERUSER_ID, company_ids, context):
            for key, value in ref_rights.iteritems():
                vals = {'code': key, 'name': value, 'company_id': company.id}
                refright_obj.create(cr, SUPERUSER_ID, vals, context)
        
        return True
    
    def name_get(self, cr, uid, ids, context=None):
        res = []
        for record in self.browse(cr, uid, ids, context):
            name = ''
            
            if record.company_id.name:
                name += '%s - ' % (record.company_id.name)
            
            name += '%s' % (record.name)
            
            res.append((record.id, name))
        
        return res
    
    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=20):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            ids = self.search(cr, uid, ['|',('name', operator, name),('company_id.name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)
    
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        _logger.warn(args)
        refright_ids = args[0][2]
        refrights = self.browse(cr, uid, refright_ids, context)
        
        company_ids = []
        for refright in refrights:
            company_ids.append(refright.company_id.id)
        
        args = [['company_id', 'not in', company_ids]]

        return super(Reference_right, self).search(cr, uid, args, offset, limit, order, context=context, count=count)
    
    _columns = {
        'name': fields.char(string='Reference_right', size=128),          
        'code': fields.char(string='Code', size=128),          
        'company_id': fields.many2one('res.company', 'Company'),
        'partner_ids': fields.many2many('res.partner', id1='referenceright', id2='partner_id', string='Partners'),
    }
    
    _sql_constraints = [
        ('company_code_unique', 'unique(company_id, code)', 'This company already has a reference right with this code.')
    ]
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: