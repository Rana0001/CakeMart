from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(
        auto_created=True, primary_key=True, unique=True)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=250, blank=True)
    product_category = models.CharField(max_length=25)
    product_price = models.CharField(max_length=10)
    product_picture = models.FileField(
        upload_to='product', blank=True)

    class Meta:
        db_table = 'product_tbl'
