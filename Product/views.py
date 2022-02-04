
from django.shortcuts import render

# Create your views here.


def productTable(request):
    return render(request, 'product/product.html')


def addProduct(request):
    return render(request, 'product/forms.html')
