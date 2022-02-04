from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True,unique=True)
    customer_first = models.CharField(max_length=25)
    customer_last = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    customer_gender = models.CharField(max_length=10)
    customer_contact = models.CharField(max_length=10)
    customer_picture = models.FileField(
        upload_to='user_profile', default="userprofile.jpg")

    class Meta:
        db_table = 'customer_tbl'
