from django.urls import path, include
from .views import CityView, StreetView, ShopView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'city', CityView, basename='get_city')
router.register('city/(?P<city_id>.+)/street', StreetView, basename='get_street_by_city_id')
router.register(r'shop', ShopView, basename='shop_create')

urlpatterns = [
    path('', include(router.urls)),
]
