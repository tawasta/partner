from odoo import models
import logging


class ResPartner(models.Model):

    _inherit = "res.partner"


    def _get_name(self):
        """ Utility method to allow name_get to be overrided without re-browse the partner """
        partner = self
        name = partner.name or ''

        if partner.company_name or partner.parent_id:
            logging.info("=====1======");
            if not name and partner.type in ['invoice', 'delivery', 'other']:
                name = dict(self.fields_get(['type'])['type']['selection'])[partner.type]
            if not partner.is_company:
                name = self._get_contact_name(partner, name)
        if self._context.get('show_address_only'):
            logging.info("=====2======");
            name = partner._display_address(without_company=True)
        if self._context.get('show_address'):
            logging.info("=====3======");
            name = name + "\n" + partner._display_address(without_company=True)
        name = name.replace('\n\n', '\n')
        name = name.replace('\n\n', '\n')
        if self._context.get('address_inline'):
            logging.info("=====4======");
            splitted_names = name.split("\n")
            name = ", ".join([n for n in splitted_names if n.strip()])
        if self._context.get('show_email') and partner.email:
            logging.info("=====5======");
            name = "%s <%s>" % (name, partner.email)
        if self._context.get('html_format'):
            logging.info("=====6======");
            name = name.replace('\n', '<br/>')
        if self._context.get('show_vat') and partner.vat:
            logging.info("=====7======");
            name = "%s ‒ %s" % (name, partner.vat)

        if not self._context.get('show_address_only') and not self._context.get('show_address') and not self._context.get('address_inline'):
            logging.info("=====8======");
            name = "%s ‒ %s" % (name, partner.id)
        return name
