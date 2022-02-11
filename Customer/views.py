
from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib import messages, auth
from authenticate import *
# Create your views here.


# @Authentication.valid_customer
def index(request):
    title = {"index": "CakeMart | Welcome to CakeMart"}
    return render(request, 'index.html', title)


@Authentication.valid_customer
def logIndex(request):
    email = request.session['email']
    userdata = Customer.objects.get(email=email)
    Customer.objects.filter(email=email).update(is_login=True)
    title = {"index": "CakeMart | Welcome to CakeMart"}
    return render(request,  'index.html', {'userdata': userdata, 'title': title})


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
                print(form)
                # request.session['customer_id'] = form.customer_id
                return redirect("/login/")
        else:
            print(form)
            print("Data Invalid")
    return render(request, 'register/register.html')


def login(request):
    if request.method == "POST":
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        email = request.POST['email']
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
# @Authentication.valid_customer
def update(request, customer_id):
    userdata = Customer.objects.get(customer_id=customer_id)
    email = request.session['email']
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=userdata)
        form.save()
        Customer.objects.filter(email=email).update(is_login=True)
        print(form)
        # request.session['customer_id'] = form.customer_id
        return redirect("/index/")
    else:
        return render(request, 'update/update.html', {'userdata': userdata})


def logout(request):
    email = request.session['email']
    Customer.objects.filter(email=email).update(is_login=False)
    request.session.flush()
    return redirect('/')
