# Generated by Django 5.1.2 on 2025-01-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_remove_productmodel_product_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
