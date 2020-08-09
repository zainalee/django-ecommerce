from django.db import models
from django.contrib.auth.models import User
from profiles.models import SellerProfile, ClientProfile
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
# from django.db import models
# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=False, null=True, blank=False)
    minorder = models.CharField(
        max_length=150, help_text='Minum Products that want to sell on per order', null=True, default=None, blank=True)
    image = models.ImageField()

    category = models.ForeignKey(
        Categories, default=1, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    @property
    def get_price(self):
        price = self.price
        return price


def pre_save_product_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username + "-" + instance.title)


pre_save.connect(pre_save_product_post_receiever, sender=Product)


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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    # product = models.ManyToManyField(OrderItem)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum(item.get_total for item in orderitem)
        return total

    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitem)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        price = self.product.price
        quantity = self.quantity
        total = price*quantity
        print(total)

        return total


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)
    date_orderd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


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
