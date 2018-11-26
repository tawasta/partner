# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class account_analytic_account(osv.osv):

    _inherit = "account.analytic.account"

    def _prepare_invoice_data(self, cr, uid, contract, context=None):
        ''' Call super to get the invoice values provided by core modules, and then add some
        additional ones '''
        res = super(account_analytic_account, self)._prepare_invoice_data(cr, uid, contract, context)
        
        res.update({
            'name_extension': contract.partner_id.name_extension,
        })
        
        return res