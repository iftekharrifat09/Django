from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            print(album_form.cleaned_data)
            return redirect('alldata')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'album_form': album_form})
        