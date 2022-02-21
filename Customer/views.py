
from django.shortcuts import render, HttpResponse, redirect

from Order.models import Order
from .forms import *
from .models import *
from django.contrib import messages, auth
from authenticate import *
from Product.models import *
from django.core.paginator import Paginator
# Create your views here.


# @Authentication.valid_customer
def index(request):
    cake = Product.objects.filter(product_category='cake')
    cupcake = Product.objects.filter(product_category='cupcake')
    dessert = Product.objects.filter(product_category='dessert')

    title = {"index": "CakeMart | Welcome to CakeMart"}
    return render(request, 'index.html', {'cake': cake, 'cupcake': cupcake,
                                          'dessert': dessert, 'title': title})


@Authentication.valid_customer
def logIndex(request):
    email = request.session['email']
    cake = Product.objects.filter(product_category='cake')
    cupcake = Product.objects.filter(product_category='cupcake')
    dessert = Product.objects.filter(product_category='dessert')

    Customer.objects.filter(email=email).update(is_login=True)
    userdata = Customer.objects.get(email=email)
    request.session['customer_id'] = userdata.customer_id
    title = {"index": "CakeMart | Welcome to CakeMart"}

    return render(request,  'index.html', {'cake': cake, 'userdata': userdata, 'cupcake': cupcake,
                                           'dessert': dessert, 'title': title})


def register(request):
    print(request)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        email = request.POST['email']
        if form.is_valid():
            if Customer.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('/index/')
            else:
                form.save()
                # print(form)
                # request.session['customer_id'] = form.customer_id
                messages.success(request, "Account Registered Successful.")
                return redirect("/login/")
        else:
            print(form)
            print("Data Invalid")
    return render(request, 'register/register.html')


def login(request):
    if request.method == "POST":
        email = request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        Customer.objects.filter(email=email).update(is_login=True)
        # try:
        return redirect('/index/')
        # except:
        #     print(request.POST)
    return render(request, 'login/login.html')


# @Authentication.valid_product_where_id
def about(request):
    return render(request, 'about_us/aboutUs.html')


# @Authentication.valid_product_where_id
def contact(request):
    return render(request, 'about_us/contact_us.html')


@Authentication.user_only
def update(request, customer_id):
    userdata = Customer.objects.get(customer_id=customer_id)
    email = request.session['email']
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=userdata)
        print(request.POST)
        form.save()
        Customer.objects.filter(email=email).update(is_login=True)
        print(form)
        request.session.flush()
        messages.success(request, "Account Updated Successful")
        return redirect("/login/")
    else:
        return render(request, 'update/update.html', {'userdata': userdata})


def logout(request):
    email = request.session['email']
    Customer.objects.filter(email=email).update(is_login=False)
    request.session.flush()
    return redirect('/')


def carditem(request):
    product = Product.objects.all()
    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    return render(request, 'card-slides/card-items.html', {'products': paged_product})


