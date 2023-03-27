# Generated by Django 4.1.7 on 2023-03-27 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_street_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='street',
        ),
        migrations.AddField(
            model_name='street',
            name='street',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='shop_street', to='backend.shop'),
            preserve_default=False,
        ),
    ]
