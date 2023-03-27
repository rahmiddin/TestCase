from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='city name')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citys'

    def __str__(self):
        return f'{self.name}'


class Street(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='street name')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='street')

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    def __str__(self):
        return f'{self.name}'


class Shop(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='shop name')
    city = models.ManyToManyField(City, related_name='city_shop')
    street = models.ForeignKey(Street, related_name='street_shop', on_delete=models.CASCADE)
    building = models.CharField(max_length=20, verbose_name='shop_building')
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        verbose_name = 'Shops'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return f'{self.name}'
