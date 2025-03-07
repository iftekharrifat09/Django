# Generated by Django 5.1.2 on 2025-02-28 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together={('brand', 'model')},
        ),
    ]
