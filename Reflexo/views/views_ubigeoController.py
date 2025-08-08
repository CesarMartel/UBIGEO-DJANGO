from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Country, Region, Province, District

@api_view(['GET'])
def regions(request):
    data = Region.objects.values('id', 'name')
    return Response(list(data))

@api_view(['GET'])
def provinces(request, region_id):
    data = Province.objects.filter(region_id=region_id).values('id', 'name')
    return Response(list(data))

@api_view(['GET'])
def districts(request, province_id):
    data = District.objects.filter(province_id=province_id).values('id', 'name')
    return Response(list(data))

@api_view(['GET'])
def countries(request):
    data = Country.objects.values('id', 'name', 'phone_code', 'ISO2')
    return Response(list(data))