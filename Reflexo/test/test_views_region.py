import pytest
from django.urls import reverse
from Reflexo.models import Region

@pytest.mark.django_db
def test_list_regions(client):
    Region.objects.create(name="Sierra")
    url = reverse("list_regions")
    response = client.get(url)
    assert response.status_code == 200

    data = response.json()
    names = [reg["name"] for reg in data]
    assert "Sierra" in names
