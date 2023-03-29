from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', )
        read_only_fields = ('id',)


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = ('id', 'name', 'city')
        read_only_fields = ('id',)


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=True)
    street = StreetSerializer(many=True)
    active = serializers.ReadOnlyField()

    class Meta:
        model = Shop
        fields = ('id', 'name', 'city', 'street', 'building', 'opening_time', 'closing_time', 'active')
        read_only_fields = ('id', )
