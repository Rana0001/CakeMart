from django.test import TestCase
from django.urls import reverse, resolve

from django.test import SimpleTestCase

from .views import *

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_orders_url(self):
        url = reverse("addProduct")
        self.assertEquals(resolve(url).func, addProduct)
