from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from .models import Province
from django.views import View

class ProvinceListView(View):
    def get(self, request):
        provinces = Province.objects.all()
        data = [{"id": province.id, "name": province.name} for province in provinces]
        return JsonResponse(data, safe=False)