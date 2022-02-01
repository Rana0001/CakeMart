

from django.shortcuts import redirect, render

from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.models import User

# Create your views here.


# def adminLogin(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             print(email)

#             return redirect("/")
#     return render(request, "admin/admin.html")

# def adminLogin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You are now logged in.')
#             return redirect('/')
#         else:
#             messages.error(request, "Invalid login credentials")
#             return redirect('/admin/login')
#     return render(request, 'admin/admin.html')
