# Generated by Django 4.0.1 on 2022-02-20 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
        ('Product', '0002_alter_product_product_desc_and_more'),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_state',
        ),
        migrations.AddField(
            model_name='order',
            name='order_quantity',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Customer.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
    ]
