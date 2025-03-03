from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_cars, name='home'),
    path('brand-filter/<slug:brand_slug>', views.all_cars, name="filter_car"),
    path('cars/', include('cars.urls')),
    path('customers/',include('customers.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

