from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from .models import City, Street, Shop
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CityView(viewsets.ReadOnlyModelViewSet):
    """To get a city"""
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def handle_exception(self, exc):
        return Response({'status': '400'}, status=400)


class StreetView(viewsets.ReadOnlyModelViewSet):
    """To get a street"""
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Street.objects.all().filter(city=city_id).only('city')

    def handle_exception(self, exc):
        return Response({'status': '400'}, status=400)


class ShopView(viewsets.ModelViewSet):
    """Create/get a shop"""
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'street']
    lookup_field = 'name'

    def get_queryset(self):
        queryset = Shop.objects.all()
        return queryset

    def handle_exception(self, exc):
        return Response({'status': '400'}, status=400)