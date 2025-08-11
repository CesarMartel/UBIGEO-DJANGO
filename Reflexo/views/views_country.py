from django.http import JsonResponse
from django.views import View
from Reflexo.models import Country

class CountryView(View):
    def get(self, request):
        countries = Country.objects.values('id', 'name', 'phone_code', 'ISO2')
        return JsonResponse(list(countries), safe=False)