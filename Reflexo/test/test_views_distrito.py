from django.test import TestCase, Client
from django.urls import reverse
from Reflexo.models import District, Province, Region
import json

class DistrictModelTest(TestCase):
    def setUp(self):
        self.region = Region.objects.create(name="Costa")
        self.province = Province.objects.create(name="Lima", region=self.region)
        self.district = District.objects.create(name="Miraflores", province=self.province)

    def test_district_creation(self):
        self.assertEqual(self.district.name, "Miraflores")
        self.assertEqual(self.district.province.name, "Lima")

    def test_str_method(self):
        self.assertEqual(str(self.district), "Miraflores")

class DistrictViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.region = Region.objects.create(name="Costa")
        self.province = Province.objects.create(name="Lima", region=self.region)
        self.district = District.objects.create(name="Miraflores", province=self.province)

    def test_district_view(self):
        response = self.client.get('/api/districts/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(len(data) > 0)
        self.assertEqual(data[0]['name'], 'Miraflores')
        self.assertEqual(data[0]['province__name'], 'Lima')
