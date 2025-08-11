import pytest
from django.urls import reverse
from Reflexo.models import Province, Region

@pytest.mark.django_db
def test_list_provinces(client):
    region = Region.objects.create(name="Costa")
    Province.objects.create(name="Lima", region=region)

    url = reverse("api_provinces")
    response = client.get(url)
    assert response.status_code == 200

    data = response.json()
    names = [prov["name"] for prov in data]
    assert "Lima" in names
