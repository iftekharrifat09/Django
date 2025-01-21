from django.shortcuts import render, redirect
from itertools import chain
from django.http import HttpResponse
from . import forms
from album.models import Album
from . import  models

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
       musician_form = forms.MusicianForm(request.POST)
       if musician_form.is_valid():
            musician_form.save()
            print(musician_form.cleaned_data)
            return redirect('alldata')  # Redirect to showdata page after saving the musician
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'musician_form': musician_form})

def add_instrument(request):
    if request.method == 'POST':
        instrument_form = forms.InstrumentForm(request.POST)
        if instrument_form.is_valid():
            instrument_form.save()
            print(instrument_form.cleaned_data)
            return redirect('alldata')
    else:
        instrument_form = forms.InstrumentForm()
    instruments = models.Instruments.objects.all()
    return render(request, 'add_instruments.html', {'instrument_form': instrument_form, 'instruments':instruments})

def showingData(request):
    musicians = models.Musician.objects.all()
    return render(request, 'showdata.html', {'musicians': musicians})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('alldata')
    else:
        musician_form = forms.MusicianForm(instance=musician)
    return render(request, 'add_musician.html', {'musician_form': musician_form})

def delete_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('alldata')