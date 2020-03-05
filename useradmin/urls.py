from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('Clientlogin', views.Clientlogin, name='Clientlogin'),
    path('logout', views.logoutuser, name='logout'),
    path('products', views.products, name='products'),
    path('createproduct/', views.createproduct, name='createproduct'),
    path('updateproduct/<str:pk>', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<str:pk>', views.deleteproduct, name='deleteproduct'),
    path('registration', views.registration, name='registration'),
    path('Clientregistration', views.ClientRegistration, name='ClientRegistration')
]
