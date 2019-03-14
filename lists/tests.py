from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page 

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/') 
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() # 1
        response = home_page(request) # 2
        html = response.content.decode('utf8') # 3
        self.assertTrue(html.startswith('<html>')) # 4
        self.assertIn('<title>To-Do lists</title>', html) # 5
        self.assertTrue(html.endswith('</html>') )# 4

