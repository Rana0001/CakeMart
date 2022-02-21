
from django.shortcuts import redirect, render
from django.contrib.auth import *
from django.contrib import messages
from Customer.models import Customer
from Order.models import Order
from .models import AdminUser
from .forms import AdminUserForm
from authenticate import *
from Product.models import *
from django.core.paginator import Paginator

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

        request.session.clear()
        username = request.session['username'] = request.POST.get('username')
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
    paginator3 = Paginator(customers, 5)
    customerpage = request.GET.get('page')
    paged_customer = paginator3.get_page(customerpage)
    return render(request, 'customer/customer.html', {'customers': paged_customer})


@Authentication.valid_admin
def home(request):
    context = {}

    customers = Customer.objects.all()
    product = Product.objects.all()
    order = AdminUser.objects.all()
    orders = Order.objects.all()

    # Order page paginator

    # Product page paginator

    # Customer pae paginator

    username = request.session['username']
    admin_users = AdminUser.objects.get(username=username)
    total_user = customers.count()
    total_product = product.count()
    total_order = orders.count()
    return render(request, "admin/base.html", {"admin_users": admin_users, 'total_customers': total_user, 'total_products': total_product, 'total_orders': total_order})


@Authentication.valid_admin_where_id
def editprofile(request, p_id):
    admin = AdminUser.objects.get(user_id=p_id)
    if request.method == "POST":
        form = AdminUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/admin/index")
    return render(request, 'admin/edit.html', {'admin': admin})
