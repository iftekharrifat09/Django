from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import models
from . import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



# Create your views here.

@method_decorator(login_required, name='dispatch')
class CreateAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('album_page')
    
    def form_valid(self, form):
        try:
            musician = models.Musician.objects.get(user=self.request.user)
            form.instance.musician = musician  # ✅ Assign the correct instance
        except models.Musician.DoesNotExist:
            return HttpResponse("You need to be a musician to create an album.")
        
        return super().form_valid(form)
    
class UpdateAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('album_page')
    
    
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('album_page')
    
def all_albums(request):
    albums = models.Album.objects.all()
    print(albums)
    return render(request, 'home.html', {'albums': albums})