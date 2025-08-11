from django.contrib import admin
from django.urls import path
from Reflexo.views.views_region import RegionView
from Reflexo.views.views_provincia import ProvinceView
from Reflexo.views.views_distrito import DistrictView
from Reflexo.views.views_country import CountryView
from Reflexo.views.views_web import HomeView, RegionsWebView, ProvincesWebView, DistrictsWebView, CountriesWebView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/regions/', RegionView.as_view(), name='list_regions'),
    path('api/provinces/', ProvinceView.as_view(), name='list_provinces'),
    path('api/districts/', DistrictView.as_view(), name='list_districts'),
    path('api/countries/', CountryView.as_view(), name='list_countries'),
    
    # Web views
    path('', HomeView.as_view(), name='home'),
    path('regions/', RegionsWebView.as_view(), name='regions_view'),
    path('provinces/', ProvincesWebView.as_view(), name='provinces_view'),
    path('districts/', DistrictsWebView.as_view(), name='districts_view'),
    path('countries/', CountriesWebView.as_view(), name='countries_view'),
]