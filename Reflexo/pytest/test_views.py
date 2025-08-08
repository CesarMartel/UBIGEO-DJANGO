import pytest
from django.urls import reverse
from Reflexo.models import Country  # ✅ Importar el modelo real

@pytest.mark.django_db
def test_list_countries(client):
    # Crear datos de prueba
    Country.objects.create(name="Peru", phone_code="+51", ISO2="PE")
    Country.objects.create(name="Mexico", phone_code="+52", ISO2="MX")

    # Ejecutar petición
    url = reverse("list_countries")
    response = client.get(url)

    # Validar respuesta
    assert response.status_code == 200
    data = response.json()

    # Solo deben aparecer países activos
    names = [country["name"] for country in data]
    assert "Peru" in names
    assert "Mexico" in names
    assert "Argentina" not in names
