from django.urls import path, include
from products.api.views import ProductViewSet, CategoryViewSet,ProductAPIView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('productlist',ProductAPIView.as_view())
]
