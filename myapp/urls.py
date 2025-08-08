from django.contrib import admin
from django.urls import path, include  # Importa include aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Incluye correctamente las rutas de la app
]