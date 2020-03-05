from products.models import Product, Categories
from rest_framework import serializers


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title')


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description',
                  'price', 'quantity', 'category', 'minorder', 'image', 'user')
