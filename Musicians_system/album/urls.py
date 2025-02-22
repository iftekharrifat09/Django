from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_albums, name="album_page"),
    path('album-form/', views.CreateAlbumView.as_view(), name="album_form"),
    path('edit-album/<int:id>', views.UpdateAlbumView.as_view(), name="edit_album"),
    path('delete-album/<int:id>', views.DeleteAlbumView.as_view(), name="delete_album"),
]