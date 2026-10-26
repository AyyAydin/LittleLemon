from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        Menu.objects.create(
            Title="Greek Salad",
            Price=Decimal("12.99"),
            Inventory=20,
        )
        Menu.objects.create(
            Title="Pasta",
            Price=Decimal("15.50"),
            Inventory=30,
        )
        Menu.objects.create(
            Title="IceCream",
            Price=Decimal("8.00"),
            Inventory=10,
        )

    def test_getall(self):
        response = self.client.get(reverse("menu-items"))

        self.assertEqual(response.status_code, 200)

        items = Menu.objects.all().order_by("pk")
        expected_data = MenuSerializer(items, many=True).data

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data, expected_data)