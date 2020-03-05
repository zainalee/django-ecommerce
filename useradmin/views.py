from django.shortcuts import render, redirect
from products.models import *
# Create your views here.
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from templates.gui.forms import UserForm, SellerFrom, ProductForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decoraters import unauthenticated, allowed_users
from profiles.models import SellerProfile
from django.contrib.auth.models import PermissionsMixin


@login_required(login_url='login')
@allowed_users(allowed_roles=['sellers'])
def home(request):
    # user = User.objects.filter(user=request.user)
    # context = {'user': user}
    product = Product.objects.filter(user=request.user).count()
    context = {
        'product': product
    }
    return render(request, 'gui/home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sellers'])
def products(request):
    products = Product.objects.filter(user=request.user)
    context = {'products': products}
    return render(request, 'gui/products.html', context)


@unauthenticated
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = SellerProfile
        user = authenticate(
            request, username=username, password=password)
        if user is not None:
            # if user.role == "seller_profile":
            auth_login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'gui/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


@unauthenticated
def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        sellerFrom = SellerFrom(request.POST)
        if form.is_valid() and sellerFrom.is_valid():
            user = form.save()
            seller = sellerFrom.save()
            seller.user = user
            seller.save()
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            gorup = Group.objects.get(name='sellers')
            user.groups.add(gorup)
            messages.success(request, 'account was created for' + username)
            # form = UserForm()
            # sellerFrom = SellerFrom()
            return redirect('login')
    else:
        form = UserForm()
        sellerFrom = SellerFrom()

    context = {'form': form, 'sellerForm': sellerFrom}
    return render(request, 'gui/signup.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sellers'])
def createproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('products')
        # instance.save()
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'gui/createproduct.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sellers'])
def updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(request.POST, instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'gui/updateproduct.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sellers'])
def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'product': product}
    return render(request, 'gui/deleteproduct.html', context)


# @unauthenticated
# def ClientRegistration(request):
#     form = UserForm()
#     print('welcome to client view')
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         print('method checked')
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             print('form processed')
#             # password = form.cleaned_data.get('password1')
#             # gorup = Group.objects.get(name='clients')
#             # user.groups.add(gorup)
#             messages.success(request, 'account was created for' + username)
#             # form = UserForm()
#             return redirect('clientlogin')
#     else:
#         form = UserForm()
#     context = {'form': form}
#     return render(request, 'gui/ClientSignUp.html', context)

@unauthenticated
def ClientRegistration(request):
    print('view called')
    cform = UserForm()
    if request.method == 'POST':
        cform = UserForm(request.POST)
        print('method checked')
        if cform.is_valid():
            cform.save()
            print('form saved successfully')
            return redirect('Clientlogin')
    else:
        print('method not checked')

    # form = UserForm()
    context = {
        'cform': cform
    }
    return render(request, 'gui/ClientSignUp.html', context)


@unauthenticated
def Clientlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = SellerProfile
        user = authenticate(
            request, username=username, password=password)
        if user is not None:
            # if user.role == "seller_profile":
            auth_login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'gui/Clientlogin.html', context)
