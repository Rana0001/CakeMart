
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from administrator.models import AdminUser
from authenticate import *
# Create your views here.


@Authentication.valid_admin
def productTable(request):
    context = {}
    users = AdminUser.objects.all()
    products = Product.objects.all()
    username = request.session['username']
    admin_users = AdminUser.objects.get(username=username)
    return render(request, 'product/product.html', {'products': products, 'users': users, 'admin_user': admin_users})


@Authentication.admin_only
@Authentication.valid_admin
def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("/admin/product/")
        else:
            return redirect("/admin/addProduct/")
    return render(request, 'product/forms.html')


@Authentication.admin_only
def editProduct(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        form.save()
        return redirect("/admin/product")
    else:
        return render(request, "product/edit.html", {'product': product})


@Authentication.valid_admin
@Authentication.admin_only
def deleteProduct(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect('/admin/product/')
