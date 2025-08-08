"""
URL configuration for Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Reflexo import views  # 👈 importar tus vistas
from Reflexo.views import views_web

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Páginas web
    path('', views_web.home_view, name='home'),
    path('countries/', views_web.countries_view, name='countries_view'),
    path('regions/', views_web.regions_view, name='regions_view'),
    path('provinces/', views_web.provinces_view, name='provinces_view'),
    path('districts/', views_web.districts_view, name='districts_view'),
    
    # API endpoints
    path('api/countries/', views_web.api_countries, name='api_countries'),
    path('api/regions/', views_web.api_regions, name='api_regions'),
    path('api/provinces/', views_web.api_provinces, name='api_provinces'),
    path('api/districts/', views_web.api_districts, name='api_districts'),
    
    # URLs originales (mantener compatibilidad)
    path("countries-api/", views.list_countries, name="list_countries"),
    path("provinces-api/", views.ProvinceListView.as_view(), name="list_provinces"),
    path("regions-api/", views.RegionView.as_view(), name="list_regions"),
]
