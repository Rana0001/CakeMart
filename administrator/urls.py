
from django.urls import path, include
from . import views
from Product.views import addProduct, deleteProduct, editProduct, productTable
urlpatterns = [
    path('index/', views.home, name="adminHome"),
    path('adduser/', views.create, name="createUser"),
    path('customer/', views.customerboard, name="customerBoard"),
    path('addProduct/', addProduct, name='addProduct'),
    path('product/', productTable, name='product'),
    path('editProduct/<product_id>', editProduct, name="editProduct"),
    path('deleteProduct/<product_id>',
         deleteProduct, name="deleteProduct"),
    # path('loginredirect/', views.redirectLogin, name="loginAdmin"),
    path('login/', views.loginAdmin, name="loginAdmin"),
    path('logout/', views.signout, name="signout"),
    path('', views.loginAdmin, name="loginAdmin"),



]
