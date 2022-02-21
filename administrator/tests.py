from django.test import TestCase

# Create your tests here.

from django.urls import reverse,resolve

from django.test import SimpleTestCase

from .views import *
from Product.views import addProduct


class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url=reverse("adminHome")
        self.assertEquals(resolve(url).func,home)

    def test_checkout_url(self):
        url=reverse("createUser")
        self.assertEquals(resolve(url).func,create)

    def test_customerboard_url(self):
        url=reverse("customerBoard")
        self.assertEquals(resolve(url).func,customerboard)

    def test_addproduct_url(self):
        url=reverse("addProduct")
        self.assertEquals(resolve(url).func,addProduct)


