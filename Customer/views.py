
from django.shortcuts import render, HttpResponse, redirect
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    print(request)
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect("/login/")
        else:
            print(form)
            print("Data Invalid")
    return render(request, 'register/register.html')


def login(request):
    return render(request, 'login/login.html')
