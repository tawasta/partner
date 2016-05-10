# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):
    
    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods
    @api.multi
    def write(self, values):
        user = self.user_id.browse([self._uid]).partner_id

        for field in values:

            if isinstance(values[field], str):
                field_name = self.fields_get()[field]['string']

                msg = "<p>"
                msg += "<b>%s</b> " % user.name
                msg += _("changed value for")
                msg += " <b>%s</b>:<br/>" % field_name
                msg += _("from")
                msg += " <b>%s</b><br/>" % getattr(self, field)
                msg += _("to")
                msg += " <b>%s</b> " % values[field]

                self.message_post(msg)

        result = super(ResPartner, self).write(values)

        return result

    # 7. Action methods

    # 8. Business methods
