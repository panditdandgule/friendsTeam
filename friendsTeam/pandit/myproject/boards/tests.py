from django.urls import reverse,resolve
from django.test import TestCase
from boards.views import home


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """In the second test, we are making use of the resolve function.
        Django uses it to match a requested URL with a list of URLs listed in the urls.py.
        This test will make sure the URL /, which is the root URL, is returning the home view."""
        view = resolve('/')
        self.assertEquals(view.func, home)