import pytest
from django.urls import reverse
from Reflexo.models import District, Province, Region

@pytest.mark.django_db
def test_list_districts(client):
    region = Region.objects.create(name="Costa")
    province = Province.objects.create(name="Lima", region=region)
    District.objects.create(name="Miraflores", province=province)

    url = reverse("api_districts")
    response = client.get(url)
    assert response.status_code == 200

    data = response.json()
    names = [dist["name"] for dist in data]
    assert "Miraflores" in names
