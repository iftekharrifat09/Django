# Generated by Django 5.1.2 on 2025-03-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(1, '⭐ (1 Star)'), (2, '⭐⭐ (2 Stars)'), (3, '⭐⭐⭐ (3 Stars)'), (4, '⭐⭐⭐⭐ (4 Stars)'), (5, '⭐⭐⭐⭐⭐ (5 Stars)')], default=3),
        ),
    ]
