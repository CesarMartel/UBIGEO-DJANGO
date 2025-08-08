from django.urls import path
from .views import RegionView

urlpatterns = [
    path('regions/', RegionView.as_view(), name='regions'),
]
