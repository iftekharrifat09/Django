# Generated by Django 5.1.2 on 2025-01-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taskCategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=50)),
                ('task_description', models.TextField()),
                ('task_completed', models.BooleanField(default=False)),
                ('task_assign_date', models.DateTimeField()),
                ('category', models.ManyToManyField(to='taskCategory.category')),
            ],
        ),
    ]
