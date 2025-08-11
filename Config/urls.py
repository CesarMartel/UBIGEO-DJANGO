from django.contrib import admin
from django.urls import path, include
from Reflexo.views.views_web import home_view, countries_view, regions_view, provinces_view, districts_view
from Reflexo.views.views_web import api_countries, api_regions, api_provinces, api_districts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('countries/', countries_view, name='countries_view'),
    path('regions/', regions_view, name='regions_view'),
    path('provinces/', provinces_view, name='provinces_view'),
    path('districts/', districts_view, name='districts_view'),
    
    # API endpoints
    path('api/countries/', api_countries, name='api_countries'),
    path('api/regions/', api_regions, name='api_regions'),
    path('api/provinces/', api_provinces, name='api_provinces'),
    path('api/districts/', api_districts, name='api_districts'),
]