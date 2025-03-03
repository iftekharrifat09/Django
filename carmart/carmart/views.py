from django.shortcuts import render
from cars.models import Car,Brand
# Create your views here.
def home(request):
    return render(request, 'home.html')


def all_cars(request, brand_slug=None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug=brand_slug)
        data = data.filter(brand=brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'data': data, 'brands':brands})