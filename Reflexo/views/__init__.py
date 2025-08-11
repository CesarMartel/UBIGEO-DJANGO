# Reflexo/views/__init__.py

# Países
from .views_country import CountryView

# Provincias
from .views_provincia import ProvinceView

# Regiones
from .views_region import RegionView

# Distritos
from .views_distrito import DistrictView

# Vistas web
from .views_web import (
    HomeView,
    CountriesWebView,
    RegionsWebView,
    ProvincesWebView,
    DistrictsWebView
)
