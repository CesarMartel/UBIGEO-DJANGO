import pytest
from Reflexo.models import Country

@pytest.mark.django_db
def test_list_countries(client):
    # ROJO: sin datos
    response = client.get('/api/countries/')
    assert response.status_code == 200
    assert response.json() == []

    # VERDE: con datos
    Country.objects.create(name="Perú", phone_code="+51", ISO2="PE")
    Country.objects.create(name="Argentina", phone_code="+54", ISO2="AR")

    response = client.get('/api/countries/')
    data = response.json()

    assert len(data) == 2
    assert data[0]['name'] == "Perú"
    assert data[1]['ISO2'] == "AR"
