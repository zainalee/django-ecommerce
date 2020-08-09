from django import forms
from profiles.models import ClientProfile, SellerProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from products.models import Product


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password': None,
            'password2': None,
        }

    def save(self, commit=False):
        user = super().save()

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SellerFrom(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = ['city', 'cnic', 'address', 'state', 'shop_name', 'mobileNo']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }


class CLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }

# class ClientForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','email','password']

#     def save(self,commit=False):
#         user=super.save()
#         user.email=self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price',
                  'quantity', 'category', 'minorder', 'image']
