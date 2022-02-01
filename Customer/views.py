
from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib import messages, auth

# Create your views here.


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
                return redirect("/login/")
        else:
            print(form)
            print("Data Invalid")
    return render(request, 'register/register.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_super:
                    auth.login(request,user)
                    return redirect("/")
        except:
            user = Customer.objects.get(email=email, password=password)

            if user is not None:
                return redirect("/")
        
        messages.error(request, 'Please! Re-enter your email and password')
        return redirect('/login/')
    return render(request, 'login/login.html')







def about(request):
    return render(request, 'about_us/aboutUs.html')


def contact(request):
    return render(request, 'about_us/contact_us.html')
