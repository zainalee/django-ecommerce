# Generated by Django 3.0 on 2020-02-01 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileNo', models.CharField(default=1, max_length=40)),
                ('cnic', models.CharField(default=1, max_length=30)),
                ('city', models.CharField(default=1, max_length=30)),
                ('address', models.CharField(default=1, max_length=30)),
                ('state', models.CharField(default=1, max_length=30)),
                ('shop_name', models.CharField(default=1, max_length=30)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
