# Generated by Django 5.1.2 on 2025-01-31 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_monthlyemployeereport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyemployeereport',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.employee'),
        ),
    ]
