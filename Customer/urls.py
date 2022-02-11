
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from Customer.views import logIndex, logout, register, login, about, index, update

urlpatterns = [
    path('', index, name="index"),
    path('index/', logIndex, name='HomeIndex'),
    # path('Customer/', include('Customer.urls'))
    path('register/', register, name="Register"),
    path('login/', login, name="login"),
    path('about/', about, name="about"),
    path('update/<customer_id>', update, name="UserUpdate"),
    path('logout/', logout, name="Logout"),
]
