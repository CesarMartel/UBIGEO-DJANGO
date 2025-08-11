from django.shortcuts import render
from django.http import JsonResponse
from Reflexo.models import Country, Region, Province, District

def home_view(request):
    """Vista para la página principal"""
    return render(request, 'home.html')

def countries_view(request):
    """Vista para mostrar países"""
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def regions_view(request):
    """Vista para mostrar regiones"""
    regions = Region.objects.filter(deleted_at__isnull=True)
    return render(request, 'regions.html', {'regions': regions})

def provinces_view(request):
    """Vista para mostrar provincias"""
    provinces = Province.objects.all()
    regions = Region.objects.filter(deleted_at__isnull=True)
    return render(request, 'provinces.html', {
        'provinces': provinces,
        'regions': regions
    })

def districts_view(request):
    """Vista para mostrar distritos"""
    districts = District.objects.all()
    provinces = Province.objects.all()
    return render(request, 'districts.html', {
        'districts': districts,
        'provinces': provinces
    })

# API endpoints para AJAX
def api_countries(request):
    """API endpoint para países"""
    countries = Country.objects.values('id', 'name', 'phone_code', 'ISO2')
    return JsonResponse(list(countries), safe=False)

def api_regions(request):
    """API endpoint para regiones"""
    regions = Region.objects.filter(deleted_at__isnull=True).values('id', 'name')
    return JsonResponse(list(regions), safe=False)

def api_provinces(request):
    """API endpoint para provincias"""
    provinces = Province.objects.values('id', 'name', 'region__name')
    return JsonResponse(list(provinces), safe=False)

def api_districts(request):
    """API endpoint para distritos"""
    districts = District.objects.values('id', 'name', 'province__name')
    return JsonResponse(list(districts), safe=False)




