# Generated by Django 4.0.1 on 2022-02-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(default='root', max_length=100)),
                ('email', models.CharField(default='root@gmail.com', max_length=100)),
                ('password', models.CharField(default='root', max_length=8)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'admin_tbl',
            },
        ),
    ]
