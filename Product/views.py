
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
# Create your views here.


def productTable(request):
    context = {}
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})


def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("/admin/product/")
        else:
            return redirect("/admin/addProduct/")
    return render(request, 'product/forms.html')


def editProduct(request, product_id):
    product = Product.objects.get(product_id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        form.save()
        return redirect("/admin/product")
    else:
        return render(request, "product/edit.html", {'product': product})


def deleteProduct(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect('/admin/product/')
