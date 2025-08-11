# Este archivo debería contener vistas, no modelos
# Los modelos ya están definidos en Reflexo/models/

from django.shortcuts import render
from django.http import JsonResponse
from Reflexo.models import District

def list_districts(request):
    """Vista para listar distritos"""
    districts = District.objects.values('id', 'name', 'province__name')
    return JsonResponse(list(districts), safe=False)
