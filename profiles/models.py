from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class SellerProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_DEFAULT, default=None)

    # password = models.CharField(max_length=50, default=1)
    mobileNo = models.CharField(max_length=40, default=1)
    cnic = models.CharField(max_length=30, default=1)
    city = models.CharField(max_length=30, default=1)
    address = models.CharField(max_length=30, default=1)
    state = models.CharField(max_length=30, default=1)
    shop_name = models.CharField(max_length=30, default=1)

    def __str__(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User, models.SET_DEFAULT, default=None)

    # mobileNo = models.CharField(max_length=30, default=1)
    # location = models.CharField(max_length=30)
    # address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
