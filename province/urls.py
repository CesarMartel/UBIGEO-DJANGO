# myapp/urls.py
from django.urls import path
from .views import ProvinceListView

urlpatterns = [
    # Ruta para listar provincias
    path('api/provinces/', ProvinceListView.as_view(), name='province-list'),
]
