from django.contrib import admin
from django.urls import path
from Reflexo.views import (
    list_countries,
    RegionView,
    ProvinceListView,
    home_view,
    countries_view,
    regions_view,
    provinces_view,
    districts_view,
    api_countries,
    api_regions,
    api_provinces,
    api_districts,
    regions,
    provinces,
    districts,
    countries
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/countries/', list_countries, name='list_countries'),
    path('api/regions/', RegionView.as_view(), name='list_regions'),
    path('api/provinces/', ProvinceListView.as_view(), name='list_provinces'),
    path('api/districts/', api_districts, name='list_districts'),
    
    # API endpoints para AJAX
    path('api/v2/countries/', api_countries, name='api_countries'),
    path('api/v2/regions/', api_regions, name='api_regions'),
    path('api/v2/provinces/', api_provinces, name='api_provinces'),
    path('api/v2/districts/', api_districts, name='api_districts'),
    
    # API endpoints para ubigeo
    path('api/v3/regions/', regions, name='ubigeo_regions'),
    path('api/v3/provinces/<int:region_id>/', provinces, name='ubigeo_provinces'),
    path('api/v3/districts/<int:province_id>/', districts, name='ubigeo_districts'),
    path('api/v3/countries/', countries, name='ubigeo_countries'),
    
    # Vistas web
    path('', home_view, name='home'),
    path('countries/', countries_view, name='countries_view'),
    path('regions/', regions_view, name='regions_view'),
    path('provinces/', provinces_view, name='provinces_view'),
    path('districts/', districts_view, name='districts_view'),
]