from products.models import Products, Categories
from rest_framework import viewsets
from .serializers import ProductSerializers, CategoriesSerializers


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Products.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializers
    queryset = Categories.objects.all()
