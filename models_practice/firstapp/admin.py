from django.contrib import admin
from . import models
# Register models
admin.site.register(models.CustomerModel)
admin.site.register(models.ProductModel)

