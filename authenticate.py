
from django.shortcuts import redirect
from administrator.models import AdminUser
from Customer.models import Customer
from django.contrib import messages


class Authentication:
    def valid_admin(function):
        def wrap(request):
            print(request)
            try:
                AdminUser.objects.get(
                    username=request.session['username'], password=request.session['password'])
                return function(request)

            except:
                print('!!!Invalid Credential!!')
                messages.warning(
                    request, 'Note:Please! Enter valid Username and password')
            return redirect('/admin/login/')
        return wrap

    def valid_admin_where_id(function):
        def wrap(request, p_id):
            try:
                AdminUser.objects.get(
                    username=request.session['username'],
                    password=request.session['password'])
                return function(request, p_id)
            except:
                messages.warning(
                    request, 'Note:Please! Enter valid Username and password')
            return redirect('/admin/login/')
        return wrap

    def valid_customer(function):
        def wrap(request):
            print(request)
            try:
                Customer.objects.get(
                    email=request.session['email'], password=request.session['password'])
                return function(request)
            except:
                messages.error(
                    request, 'Please! Re-enter your email and password')
            return redirect('/login/')
        return wrap

    def valid_customer_where_id(function):
        def wrap(request, p_id):
            try:
                Customer.objects.get(
                    username=request.session['username'], password=request.session['password'])
                return function(request, p_id)
            except:
                messages.error(
                    request, 'Please! Re-enter your email and password')
            return redirect('/login')
        return wrap

    def valid_product_where_id(function):
        def wrap(request, product_id):
            try:
                AdminUser.objects.get(
                    username=request.session['username'],
                    password=request.session['password'])
                return function(request, product_id)
            except:
                messages.warning(
                    request, 'Note:Please! Enter valid Username and password')
            return redirect('/admin/login/')
        return wrap

    # def admin_only(view_function):
    #     def wrapper_function(request, *args, **kwargs):
            
    #         if request.user.is_staff:
    #             return view_function(request, *args, **kwargs)
    #         else:
    #             return redirect('/admin/index/')
    #     return wrapper_function