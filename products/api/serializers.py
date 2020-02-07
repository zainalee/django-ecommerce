from products.models import Products, Categories
from rest_framework import serializers


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title')


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'description',
                  'price', 'quantity', 'category', 'user')
