# -*- coding: utf-8 -*-
import logging
from openerp.osv import osv, fields
from openerp.tools.translate import _
_logger = logging.getLogger(__name__)
    
class ResPartner(osv.Model):
    _inherit = "res.partner"
    _name = "res.partner"
    
    def _get_roles(self, cr, uid, ids, field_name, arg, context=None):
        records = self.browse(cr, uid, ids)
        result = {}
        
        for record in records:
            partner_roles = []
            for role in record.company_roles:
                role_name = role.name_get()[0][1]
                partner_roles.append(role_name)
            for role in record.contact_roles:
                role_name = role.name_get()[0][1]
                partner_roles.append(role_name)
            for role in record.contact_server_roles:
                role_name = role.name_get()[0][1]
                partner_roles.append(role_name)
            
            partner_string = "\n".join(partner_roles)
            result[record.id] = partner_string.encode('utf-8')
        return result
    
    _columns = {
        'partner_roles': fields.function(_get_roles, type='char', obj='res.partner', method=True, store=False, string='Roles'),
    }
    
ResPartner()
