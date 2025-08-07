from django.urls import path
from .views import list_countries

urlpatterns = [
    path('countries/', list_countries, name='list_countries'),
]
