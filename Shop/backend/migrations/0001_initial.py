# Generated by Django 4.1.7 on 2023-03-27 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='city name')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citys',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='street name')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='street', to='backend.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='shop name')),
                ('building', models.CharField(max_length=20, verbose_name='shop_building')),
                ('opening_time', models.DateTimeField()),
                ('closing_time', models.DateTimeField()),
                ('city', models.ManyToManyField(related_name='city_shop', to='backend.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='street_shop', to='backend.street')),
            ],
        ),
    ]
