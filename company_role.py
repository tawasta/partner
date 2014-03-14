from openerp.osv import osv, fields
from tools.translate import _

class CompanyRole(osv.Model):
    _name = "res.partner.company.role"
    _columns = {
        "name": fields.char("Role name", size=64),
        "parent": fields.many2one('res.partner.company.role', 'Role parent'),
    }
CompanyRole()

class Partner(osv.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
        
    _columns = {
        'company_roles': fields.many2many(
            'res.partner.company.role',
            'res_partner_company_role_rel'
            '',
            'id',
            string=_('Company roles'),
            help='Company roles for customer grouping and searching'
        ),
    }
Partner()

class CompanyRole_update(osv.Model):
    _name = "res.partner.company.role"
    _inherit = "res.partner.company.role"
    columns = {
       "res.partner_ids": fields.one2many("res.partner", "res.partner.company.role_id", "Links"),
   }
CompanyRole_update()