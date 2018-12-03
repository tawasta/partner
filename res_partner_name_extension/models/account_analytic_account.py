# -*- coding: utf-8 -*-
from odoo import models


class account_analytic_account(models.Model):

    _inherit = "account.analytic.account"

    def _prepare_invoice_data(self, contract):
        # Call super to get the invoice values provided by core modules,
        # and then add some
        # additional ones
        res = super(account_analytic_account,
            self)._prepare_invoice_data(contract)
        
        res.update({
            'name_extension': contract.partner_id.name_extension,
        })
        
        return res
