from django.contrib import admin
from django.urls import path, include
from . import views
from album.views import all_albums

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_albums, name="home_page"),
    path('album/', include('album.urls') ),
    path('musician/', include('musician.urls') ),
]
