from .settings import *  # Importa todo desde settings.py

# Configuración específica para las pruebas (si es necesario)
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'test_db.sqlite3',  # Usa una base de datos separada para las pruebas
}

# Si es necesario, también puedes cambiar otros parámetros como EMAIL, CACHE, etc.
