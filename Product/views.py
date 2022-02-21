
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from administrator.models import AdminUser
from authenticate import *
from django.core.paginator import Paginator
# Create your views here.


@Authentication.valid_admin
def productTable(request):
    context = {}
    users = AdminUser.objects.all()
    products = Product.objects.all()
    username = request.session['username']
    admin_users = AdminUser.objects.get(username=username)
    paginator2 = Paginator(products, 5)
    productpage = request.GET.get('productpage')
    paged_product = paginator2.get_page(productpage)
    return render(request, 'product/product.html', {'products': paged_product, 'users': users, 'admin_user': admin_users})


@Authentication.valid_admin
def addProduct(request):
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Product Added Successful.")
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
