from django.urls import path, include
from profiles.api.views import SellerViewSet, BuyerViewSet
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


router = routers.DefaultRouter()
router.register('seller', views.SellerViewSet, basename='seller')
router.register('buyer', views.BuyerViewSet, basename='buyer')

# router.register('categories', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('seller', views.SellerViewSet.as_view())
]


# urlpatterns += format_suffix_patterns([
#     # API to map the student record
#     path('api/univstud/$',
#          views.SellerRecordView.as_view(),
#          name='students_list'),
# ])
