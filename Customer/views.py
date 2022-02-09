
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


def register(request):
    print(request)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        email = request.POST['email']
        if form.is_valid():
            if Customer.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('/')
            else:
                form.save()
                print(form)
                request.session['customer_id'] = form.customer_id
                return redirect("/login/")
        else:
            print(form)
            print("Data Invalid")
    return render(request, 'register/register.html')


def login(request):
    if request.method == "POST":
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('/')
    return render(request, 'login/login.html')


# @Authentication.valid_product_where_id
def about(request):
    return render(request, 'about_us/aboutUs.html')


# @Authentication.valid_product_where_id
def contact(request):
    return render(request, 'about_us/contact_us.html')
