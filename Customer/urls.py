from os import name
from django.contrib import admin
from django.urls import path, include
from Customer import views

urlpatterns = [
    path('', views.index,name="index"),
    # path('Customer/', include('Customer.urls'))
    path('register/', views.register, name="Register")
]
