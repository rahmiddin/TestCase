from django.contrib import admin
from .models import Shop, Street, City
# Register your models here.


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields = ['name', 'city', 'street', 'building', 'opening_time', 'closing_time']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    fields = ['name', 'city']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['name', ]