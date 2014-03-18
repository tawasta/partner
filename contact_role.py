from openerp.osv import osv, fields
from tools.translate import _

class res_partner_contact_role(osv.osv):

    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if context.get('partner_category_display') == 'short':
            return super(res_partner_category, self).name_get(cr, uid, ids, context=context)
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            # Be sure name_search is symmetric to name_get
            name = name.split(' / ')[-1]
            ids = self.search(cr, uid, [('name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)


    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _description = 'Contact Roles'
    _name = 'res.partner.contact.role'
    _columns = {
        'name': fields.char('Role Name', required=True, size=64, translate=True),
        'parent_id': fields.many2one('res.partner.contact.role', 'Parent Role', select=True, ondelete='cascade'),
        'complete_name': fields.function(_name_get_fnc, type="char", string='Full Name'),
        'child_ids': fields.one2many('res.partner.contact.role', 'parent_id', 'Child Roles'),
        'active': fields.boolean('Active', help="The active field allows you to hide the category without removing it."),
        'parent_left': fields.integer('Left parent', select=True),
        'parent_right': fields.integer('Right parent', select=True),
        'partner_ids': fields.many2many('res.partner', id1='category_id', id2='partner_id', string='Partners'),
    }
    _constraints = [
        (osv.osv._check_recursion, 'Error ! You can not create recursive categories.', ['parent_id'])
    ]
    _defaults = {
        'active': 1,
    }
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

res_partner_contact_role()

class res_partner(osv.osv):
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
res_partner()

class res_partner_contact_role_update(osv.Model):
    _name = "res.partner.contact.role"
    _inherit = "res.partner.contact.role"
    columns = {
       "res.partner_ids": fields.one2many("res.partner", "res.partner.contact.role_id", "Links"),
   }
res_partner_contact_role_update()