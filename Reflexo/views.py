from django.http import JsonResponse
from .models import Country

def list_countries(request):
    countries = Country.objects.filter(deleted_at__isnull=True).values('id', 'name', 'phone_code', 'ISO2')
    return JsonResponse(list(countries), safe=False)
