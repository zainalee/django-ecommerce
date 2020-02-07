from django.shortcuts import render
from products.models import *
# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'gui/home.html')


def products(request):
    products = Products.objects.all()
    return render(request, 'gui/products.html', {'products': products})


def login(request):
    return HttpResponse('login')
