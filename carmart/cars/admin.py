from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Brand)
admin.site.register(models.CarModel)
admin.site.register(models.Car)
admin.site.register(models.Comment)
