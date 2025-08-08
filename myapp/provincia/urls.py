from django.urls import path
from . import views

urlpatterns = [
    path('provincias/', views.ProvinceListView.as_view(), name='province_list'),
]
