# Generated by Django 5.1.2 on 2025-02-28 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brand'),
        ),
    ]
