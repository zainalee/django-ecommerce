from django.db import models
from django.contrib.auth.models import User
from profiles.models import SellerProfile, ClientProfile
# from django.db import models
# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)
    description = models.TextField()
    price = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    minorder = models.CharField(
        max_length=150, help_text='Minum Products that want to sell on per order', null=True, default=None, blank=True)
    image = models.ImageField()

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


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     created = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f'{self.quantity} of {self.item.name}'


class Order(models.Model):
    pass
#     orderitems  = models.ManyToManyField(Cart)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username

# user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                          on_delete=models.CASCADE)
# # ref_code = models.CharField(max_length=20, blank=True, null=True)
# items = models.ManyToManyField(Product)
# start_date = models.DateTimeField(auto_now_add=True)
# ordered_date = models.DateTimeField()
# ordered = models.BooleanField(default=False)
# # shipping_address = models.ForeignKey(
# #     'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
# # billing_address = models.ForeignKey(
# #     'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
# # payment = models.ForeignKey(
# #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
# coupon = models.ForeignKey(
#     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
# being_delivered = models.BooleanField(default=False)
# received = models.BooleanField(default=False)
# refund_requested = models.BooleanField(default=False)
# refund_granted = models.BooleanField(default=False)
