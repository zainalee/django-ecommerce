from django.db import models
from django.contrib.auth.models import User
from profiles.models import SellerProfile, ClientProfile
# from django.db import models
# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(
        SellerProfile, on_delete=models.SET_DEFAULT, default=None)
    description = models.TextField()
    price = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    # img-url=models.
    # image = models.ImageField()
    category = models.ForeignKey(
        Categories, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    description = models.CharField(max_length=150)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.rating


STATUS = (
    ('Pending', 'Pending'),
    ('Out of delivery', 'out of delivery'),
    ('Deliverd', 'Deliverd')
)


class Order(models.Model):

    user = models.ForeignKey(ClientProfile,
                             on_delete=models.CASCADE, default=None)
    # ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ForeignKey(Products, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=150, choices=STATUS)
    # start_date = models.DateTimeField(auto_now_add=True,)
    # order_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
