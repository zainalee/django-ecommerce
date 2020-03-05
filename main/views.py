from django.shortcuts import render, redirect
from products.models import *

# Create your views here.


def main(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'gui/main.html', context)
