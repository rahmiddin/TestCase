# Generated by Django 4.1.7 on 2023-03-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_shop_options_alter_street_options_city_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
