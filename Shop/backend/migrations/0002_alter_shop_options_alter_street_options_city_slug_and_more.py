# Generated by Django 4.1.7 on 2023-03-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Shops', 'verbose_name_plural': 'Shops'},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'verbose_name': 'Street', 'verbose_name_plural': 'Streets'},
        ),
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='closing_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shop',
            name='opening_time',
            field=models.TimeField(),
        ),
    ]
