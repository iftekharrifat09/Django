from django.contrib import admin
from django.urls import path, include
from . import views
from album.views import all_albums
from musician.views import LoginClassView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', all_albums, name="home_page"),
    path('', LoginClassView.as_view()),
    path('album/', include('album.urls') ),
    path('musician/', include('musician.urls') ),
]
