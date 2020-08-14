from .models import *
from django_filters import CharFilter
import django_filters


class ProductFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['image', 'user', 'description',
                   'price', 'quantity', 'minorder', 'category', 'slug', 'unit']
