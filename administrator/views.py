from django.shortcuts import redirect, render
from django.contrib.auth import *
from django.contrib import messages
from Customer.models import Customer
from .models import AdminUser
from .forms import AdminUserForm
from authenticate import *
from Product.models import *


# Create your views here.


# @Authentication.admin_only
@Authentication.valid_admin
@Authentication.admin_only
def create(request):
    if request.method == "POST":
        # try:
        form = AdminUserForm(request.POST)
        email = request.POST['email']
        username = request.POST['username']
        if form.is_valid():
            if AdminUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('/admin/adduser/')
            elif AdminUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('/admin/adduser/')
            else:
                form.save()
                print(form)
                return redirect("/admin/index/")
        # except:
        #     return redirect("/admin/index/")
    return render(request, 'admin/form.html')


# def redirectLogin(request):
#     return render(request, 'admin/login.html')


# @Authentication.valid_admin
def loginAdmin(request):
    if request.method == "POST":
        username = request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        AdminUser.objects.filter(username=username).update(is_admin=True)
        return redirect('/admin/index/')
    return render(request, 'admin/login.html')


def signout(request):
    username = request.session['username']
    AdminUser.objects.filter(username=username).update(is_admin=False)
    request.session.flush()
    return redirect('/admin/login/')


@Authentication.valid_admin
def customerboard(request):
    context = {}
    customers = Customer.objects.all()

    return render(request, 'customer/customer.html', {'customers': customers})


@Authentication.valid_admin
def home(request):
    context = {}
    customers = Customer.objects.all()
    product = Product.objects.all()
    users = AdminUser.objects.all()
    username = request.session['username']
    admin_users = AdminUser.objects.get(username=username)
    total_user = customers.count()
    total_product = product.count()
    return render(request, "admin/index.html", {"users": users, "admin_users": admin_users, 'customers': total_user, 'products': total_product})
