from django.db import models
from Customer.models import Customer
from Product.models import Product

# Create your models here.


class Order(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True,unique=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_items = models.CharField(max_length=10)
    order_date = models.DateField()
    order_address = models.CharField(max_length=25)
    payment_state = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_tbl'
