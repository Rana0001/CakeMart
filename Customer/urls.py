
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from Customer.views import carditem, logIndex, logout, register, login, about, index, update

urlpatterns = [
    path('', index, name="index"),
    path('index/', logIndex, name='HomeIndex'),
    # path('Customer/', include('Customer.urls'))
    path('register/', register, name="Register"),
    path('login/', login, name="login"),
    path('about/', about, name="about"),
    path('update/<customer_id>', update, name="UserUpdate"),
    path('logout/', logout, name="Logout"),
    path('product/', carditem, name="product"),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='login/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='login/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='login/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='login/password_reset_complete.html'),
         name='password_reset_complete'),


]
