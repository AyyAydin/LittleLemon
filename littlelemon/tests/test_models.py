from decimal import Decimal
from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            Title="IceCream",
            Price=Decimal("80.00"),
            Inventory=100,
        )

        item.refresh_from_db()

        self.assertEqual(str(item), "IceCream : 80.00")