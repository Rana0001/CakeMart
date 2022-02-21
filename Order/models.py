from django.db import models
from Customer.models import Customer
from Product.models import Product

# Create your models here.


class Order(models.Model):
    order_id = models.AutoField(
        auto_created=True, primary_key=True, unique=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    order_quantity = models.CharField(max_length=50, blank=True)
    order_date = models.DateField(blank=True)
    order_address = models.CharField(max_length=50, blank=True)
    payment_method = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'order_tbl'
