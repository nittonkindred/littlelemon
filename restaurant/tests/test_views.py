from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest (TestCase):
    def setUp(self):
        Menu.objects.create(Title="Pizza", Price=9.99, Inventory=10)
        Menu.objects.create(Title="Pasta", Price=7.99, Inventory=15)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serialized_items = MenuSerializer(menu_items, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_items)
        self.assertEqual(len(response.data), 2)