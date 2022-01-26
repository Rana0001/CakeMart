from django.forms import forms
from django.shortcuts import render,HttpResponse,redirect
from Customer.forms import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    print(request)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
                form.save()
                print(form)
                return redirect("/")
        else:
                print("Invalid Data")
                print(forms)
    return render(request,'register/register.html')