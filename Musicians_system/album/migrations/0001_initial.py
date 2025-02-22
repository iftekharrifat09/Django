# Generated by Django 5.1.6 on 2025-02-18 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0004_alter_musician_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album_release_date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (4, '4'), (3, '3'), (5, '5'), (2, '2')], default=3)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]
