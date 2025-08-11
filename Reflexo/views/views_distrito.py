from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from Reflexo.models import District

class DistrictView(View):
    def get(self, request):
        """Vista para listar distritos"""
        districts = District.objects.values('id', 'name', 'province__name')
        return JsonResponse(list(districts), safe=False)
