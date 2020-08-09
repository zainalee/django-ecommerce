from django.urls import path, include
from products.api.views import CategoryViewSet, CategoryAPIView, ProductAPIView, api_detail_product_view
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('productlist', ProductAPIView.as_view()),
    path('categorylist', CategoryAPIView.as_view()),
    # path('CheckOutSerializer', CheckOutSerializer.as_view()),
    path('<str:pk>', api_detail_product_view, name="detail")
]
