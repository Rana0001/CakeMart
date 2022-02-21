from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/<slug:product_id>', views.order_product, name="buyproduct"),
    # path('')
]
