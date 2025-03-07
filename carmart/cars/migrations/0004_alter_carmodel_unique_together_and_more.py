# Generated by Django 5.1.2 on 2025-02-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='carmodel',
            constraint=models.UniqueConstraint(fields=('brand', 'model_number'), name='unique_brand_model'),
        ),
    ]
