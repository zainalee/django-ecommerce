from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class SellerProfile(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE, default=None)

    mobileNo = models.CharField(max_length=40, default=None)
    cnic = models.CharField(max_length=30, default=None)
    city = models.CharField(max_length=30, default=None)
    address = models.CharField(max_length=30, default=None)
    state = models.CharField(max_length=30, default=None)
    shop_name = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username
