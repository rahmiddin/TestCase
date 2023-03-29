from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='city name')
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citys'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Street(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='street name')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='street')
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Shop(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='shop name')
    city = models.ManyToManyField(City, related_name='city_shop')
    street = models.ManyToManyField(Street, related_name='street_shop')
    building = models.CharField(max_length=20, verbose_name='shop_building')
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    @property
    def active(self):
        now = timezone.now().time()
        print(now)
        if self.opening_time < now < self.closing_time:
            return 1
        return 0

    class Meta:
        verbose_name = 'Shops'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return f'{self.name}'
