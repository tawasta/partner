
from openerp.osv import orm, fields
from openerp.tools.translate import _

class partner(orm.Model):

    _inherit = "res.partner"

    _columns = {
        'name_extension': fields.char('Name extension', size=128)
    }
