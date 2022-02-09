# Generated by Django 4.0.1 on 2022-02-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('customer_first', models.CharField(max_length=25)),
                ('customer_last', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25)),
                ('customer_gender', models.CharField(max_length=10)),
                ('customer_contact', models.CharField(max_length=10)),
                ('customer_picture', models.FileField(default='userprofile.jpg', upload_to='user_profile')),
                ('is_login', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'customer_tbl',
            },
        ),
    ]
