from django.urls import resolve
from django.test import TestCase
from lists.views import home_page # (2)

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/') # (1)
        self.assertEqual(found.func, home_page) #(1)

