from openerp.osv import osv, fields
from tools.translate import _

class ContactRole(osv.Model):
    _name = "res.partner.contact.role"
    _columns = {
        "name": fields.char("Role name", size=64),
        "parent": fields.many2one('res.partner.contact.role', 'Role parent'),
    }
ContactRole()

class Partner(osv.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
        
    _columns = {
        'contact_roles': fields.many2many(
            'res.partner.contact.role',
            'res_partner_contact_role_rel'
            '',
            'id',
            string=_('Contact roles'),
            help='Contact roles for contact grouping and searching'
        ),
    }
Partner()

class ContactRole_update(osv.Model):
    _name = "res.partner.contact.role"
    _inherit = "res.partner.contact.role"
    columns = {
       "res.partner_ids": fields.one2many("res.partner", "res.partner.contact.role_id", "Links"),
   }
ContactRole_update()