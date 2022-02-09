# Generated by Django 4.0.1 on 2022-02-08 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('order_items', models.CharField(max_length=10)),
                ('order_date', models.DateField()),
                ('order_address', models.CharField(max_length=25)),
                ('payment_state', models.CharField(max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
            options={
                'db_table': 'order_tbl',
            },
        ),
    ]
