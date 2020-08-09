from products.models import Product, Categories, ShippingAddress
from rest_framework import serializers


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title')


class ProductSerializers(serializers.ModelSerializer):
    # choices = ChoiceSerializer(many=True, read_only=True, required=False)
    image = serializers.SerializerMethodField('validate_image_url')
    username = serializers.SerializerMethodField('get_username_from_author')
    category = serializers.SerializerMethodField('get_category_from_product')

    class Meta:
        model = Product
        fields = ('pk', 'title', 'slug', 'description',	'price',
                  'quantity',	'minorder',	'image',	'category', 'username')

    def get_username_from_author(self, product):
        username = product.user.username
        return username

    def get_category_from_product(self, product):
        cat = product.category.title
        return cat

    def validate_image_url(self, blog_post):
        image = blog_post.image
        new_url = image.url
        if "?" in new_url:
            new_url = image.url[:image.url.rfind("?")]
        return new_url


# class CheckOutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingAddress
#         fields = ('user', 'order', 'name', 'address',
#                   'city', 'state', 'zipcode')
