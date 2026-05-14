from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Pizza", Price=9.99, Inventory=10)
        Menu.objects.create(Title="Pasta", Price=7.99, Inventory=15)

    def test_menu_item_str(self):
        pizza = Menu.objects.get(Title="Pizza")
        pasta = Menu.objects.get(Title="Pasta")
        self.assertEqual(str(pizza), "Pizza : 9.99")
        self.assertEqual(str(pasta), "Pasta : 7.99")