from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestDefaultInvoiceAddress(TransactionCase):
    def test_address_get_prefers_default_invoice_address(self):
        partner_obj = self.env["res.partner"]
        company = partner_obj.create({
            "name": "Acme Ltd",
            "is_company": True,
        })
        billing = partner_obj.create({
            "name": "Acme Ltd Billing",
            "type": "invoice",
            "parent_id": company.id,
            # address_get does not walk into child companies
            "is_company": False,
        })
        self.assertEqual(
            company.address_get(["invoice"])["invoice"],
            billing.id,
        )

        accounts = partner_obj.create({
            "name": "Acme Ltd Accounts",
            "type": "invoice",
            "parent_id": company.id,
            "is_company": False,
        })
        company.default_partner_invoice_id = accounts
        self.assertEqual(
            company.address_get(["invoice"])["invoice"],
            accounts.id,
        )
