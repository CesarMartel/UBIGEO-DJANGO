## Módulo 07 - Ubigeo y Ubicaciones 📍

### Responsabilidades
- **Modelos de ubicación**: `Country`, `Region`, `Province`, `District` y sus relaciones jerárquicas.
- **APIs (views/controllers)**: Listado y consulta de ubicaciones para integrarse con React.
- **Soporte de jerarquía**: País → Región → Provincia → Distrito.

### Meta: MVT/MVC con APIs para React
- En Django se usa MVT (Model-View-Template). Aquí las "Views" actúan como controladores de API (Django/DRF), análogo al Controller de MVC.

---

## Model (Modelos)

### Country (`Reflexo/models/country.py`)
- **Campos**:
  - `name` (CharField): Nombre del país.
  - `phone_code` (CharField): Código telefónico (p. ej., +51).
  - `ISO2` (CharField, 2 chars): Código ISO alfa-2 (p. ej., PE).
- **Relaciones auxiliares**: `CountryUser`, `CountryPatient`, `CountryTherapist` enlazan entidades del dominio con un país.

### Region (`Reflexo/models/region.py`)
- **Campos**:
  - `name` (CharField): Nombre de la región.
  - `deleted_at` (DateTimeField, null/blank): Soporte de soft delete.
- **Comportamiento**:
  - `delete()`: realiza soft delete asignando `deleted_at`.
  - `restore()`: restaura el registro limpiando `deleted_at`.
- **Relaciones auxiliares**: `RegionUser`, `RegionPatient`, `RegionTherapist`.
- **Meta**: `db_table = "region"`.

### Province (`Reflexo/models/province.py`)
- **Campos**:
  - `name` (CharField): Nombre de la provincia.
  - `region` (ForeignKey → `Region`, `related_name='provinces'`): pertenencia de la provincia a una región.
- **Relaciones auxiliares**: `ProvinceUser`, `ProvincePatient`, `ProvinceTherapist`.

### District (`Reflexo/models/district.py`)
- **Campos**:
  - `name` (CharField, default="Sin nombre"): Nombre del distrito.
  - `province` (ForeignKey → `Province`, `related_name='districts'`): pertenencia del distrito a una provincia.
- **Relaciones auxiliares**: `DistrictUser`, `DistrictPatient`, `DistrictTherapist`.

### Relaciones Jerárquicas
```
Country (País)
└── Region (Región)
    └── Province (Provincia)
        └── District (Distrito)
```

---

## View (Vistas / Controllers de API)

### Country Controllers
- Archivo: `Reflexo/views/views_country.py`
- **`list_countries(request)`** (Django view)
  - Método: GET
  - Retorna: Lista JSON de países con `id`, `name`, `phone_code`, `ISO2`.

### Region Controllers
- Archivo: `Reflexo/views/views_region.py`
- **`RegionView`** (DRF `APIView`)
  - GET: Lista regiones (`id`, `name`).
  - POST: Placeholder de ejemplo (201 con mensaje).

### Province Controllers
- Archivo: `Reflexo/views/views_provincia.py`
- **`ProvinceListView`** (Django `View`)
  - GET: Lista provincias (`id`, `name`).

### Ubigeo Controllers (API unificada)
- Archivo: `Reflexo/views/views_ubigeoController.py` (DRF function-based views)
  - `regions` (GET): Lista regiones (`id`, `name`).
  - `provinces` (GET `/<region_id>`): Provincias por región.
  - `districts` (GET `/<province_id>`): Distritos por provincia.
  - `countries` (GET): Lista países (`id`, `name`, `phone_code`, `ISO2`).
- Nota: Estas vistas existen pero aún no están registradas en `Config/urls.py`.

---

## Rutas actuales (registradas en `Config/urls.py`)
- GET `/countries/` → `list_countries`
- GET `/regions/` → `RegionView.get`
- GET `/provinces/` → `ProvinceListView.get`

## Rutas adicionales disponibles (pendientes de registrar)
Desde `views_ubigeoController.py`:
- GET `/ubigeo/regions` → Lista regiones
- GET `/ubigeo/provinces/<region_id>` → Provincias por región
- GET `/ubigeo/districts/<province_id>` → Distritos por provincia
- GET `/ubigeo/countries` → Lista países

---

## APIs a Desarrollar para React (sugerencia)
- `GET /api/countries` – Listar países
- `GET /api/countries/{id}` – Obtener país específico
- `GET /api/regions` – Listar regiones
- `GET /api/regions/{id}` – Obtener región específica
- `GET /api/regions/by-country/{country_id}` – Regiones por país
- `GET /api/provinces` – Listar provincias
- `GET /api/provinces/{id}` – Obtener provincia específica
- `GET /api/provinces/by-region/{region_id}` – Provincias por región
- `GET /api/districts` – Listar distritos
- `GET /api/districts/{id}` – Obtener distrito específico
- `GET /api/districts/by-province/{province_id}` – Distritos por provincia
- `GET /api/ubigeo/search` – Búsqueda de ubicaciones
- `GET /api/ubigeo/autocomplete` – Autocompletado de ubicaciones
- `GET /api/ubigeo/hierarchy` – Jerarquía completa de ubicaciones

> Nota: Varias ya están cubiertas parcialmente por los controllers existentes; requerirán registrar rutas y, en algunos casos, completar lógica.

---

## Estructura jerárquica de ejemplo
```
País (Perú)
├── Región (Lima)
│   ├── Provincia (Lima)
│   │   ├── Distrito (Miraflores)
│   │   ├── Distrito (San Isidro)
│   │   └── Distrito (Barranco)
│   └── Provincia (Callao)
│       ├── Distrito (Callao)
│       └── Distrito (Bellavista)
└── Región (Arequipa)
    └── Provincia (Arequipa)
        └── Distrito (Arequipa)
```

---

## Dependencias
- Django ORM para modelos y relaciones.
- Django REST Framework (DRF) para APIs.
- Pytest para tests.

---

## Entregables
- [ ] CRUD completo de ubicaciones
- [ ] API de ubigeo funcional y documentada
- [ ] Búsqueda y autocompletado
- [ ] Jerarquía de ubicaciones
- [ ] Caché de catálogos (opcional)
- [ ] Validaciones robustas
- [ ] Integración lista para React
- [ ] Tests unitarios y de integración en verde

---