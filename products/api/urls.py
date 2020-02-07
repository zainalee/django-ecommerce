from django.urls import path, include
from products.api.views import ProductViewSet, CategoryViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
