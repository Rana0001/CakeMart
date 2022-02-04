
from django.contrib import admin
from django.urls import path, include
from Customer.views import register, login, about, index

urlpatterns = [
    path('', index, name="index"),
    # path('Customer/', include('Customer.urls'))
    path('register/', register, name="Register"),
    path('login/', login, name="login"),
    path('about/', about, name="about"),

]
