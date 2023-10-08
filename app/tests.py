from django.test import TestCase
from django.urls import reverse

from app.models import MenuModel


class MenuModelTestCase(TestCase):
    def setUp(self):
        self.menu1 = MenuModel.objects.create(name='Menu 1', named_url='menu-1')
        self.menu2 = MenuModel.objects.create(name='Menu 2', named_url='menu-2', parent=self.menu1)
        self.menu3 = MenuModel.objects.create(name='Menu 3', named_url='menu-3', parent=self.menu2)

    def test_menu_model_str(self):
        self.assertEqual(str(self.menu1), 'Menu 1')
        self.assertEqual(str(self.menu2), 'Menu 2')
        self.assertEqual(str(self.menu3), 'Menu 3')


class MenuViewTestCase(TestCase):
    def setUp(self):
        self.menu1 = MenuModel.objects.create(name='Menu 1', named_url='menu-1')
        self.menu2 = MenuModel.objects.create(name='Menu 2', named_url='menu-2', parent=self.menu1)
        self.menu3 = MenuModel.objects.create(name='Menu 3', named_url='menu-3', parent=self.menu2)

    def test_menu_list_view(self):
        url = reverse('menu_list', args=[self.menu1.named_url])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<li>Menu 1')
        self.assertContains(response, '<li>Menu 2')
        self.assertContains(response, '<li>Menu 3')

