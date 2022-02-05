from django.shortcuts import redirect, render
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Customer.models import Customer
from .models import AdminUser
from .forms import AdminUserForm
# from django.contrib.auth.models import User

# Create your views here.

# def registerAdmin(request):


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


def customerboard(request):
    context = {}
    customers = Customer.objects.all()
    return render(request, 'customer/customer.html', {'customers': customers})


def home(request):

    context = {}
    users = AdminUser.objects.all()
    return render(request, "admin/index.html", {"users": users})
