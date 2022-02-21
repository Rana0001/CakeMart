from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from Product.models import *
from django.core.paginator import Paginator
# Create your views here.


def order_product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Successful")
        else:
            form = OrderForm()
    return render(request, "buypage/Buypage.html", {'product': product})


def ordertbl(request):

    order = Order.objects.raw("select * from order_tbl")
    paginator1 = Paginator(order, 5)
    orderpage = request.GET.get('page')
    paged_order = paginator1.get_page(orderpage)
    return render(request, 'order/order.html', {'order': paged_order})
