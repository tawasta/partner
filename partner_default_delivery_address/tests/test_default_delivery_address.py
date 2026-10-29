from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestDefaultDeliveryAddress(TransactionCase):
    def test_address_get_prefers_default_delivery_address(self):
        partner_obj = self.env["res.partner"]
        company = partner_obj.create({
            "name": "Example Corp",
            "is_company": True,
        })
        warehouse = partner_obj.create({
            "name": "Example Corp Warehouse",
            "type": "delivery",
            "parent_id": company.id,
            # address_get does not walk into child companies
            "is_company": False,
        })
        self.assertEqual(
            company.address_get(["delivery"])["delivery"],
            warehouse.id,
        )

        shop = partner_obj.create({
            "name": "Example Corp Shop",
            "type": "delivery",
            "parent_id": company.id,
            "is_company": False,
        })
        company.default_partner_delivery_id = shop
        self.assertEqual(
            company.address_get(["delivery"])["delivery"],
            shop.id,
        )
