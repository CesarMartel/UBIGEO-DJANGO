from django.test import TestCase
from .models import Province, Region

class ProvinceModelTest(TestCase):
    
    def setUp(self):
        self.region = Region.objects.create(name="Region 1")
        self.province = Province.objects.create(name="Province 1", region=self.region)
    
    def test_province_creation(self):
        self.assertEqual(self.province.name, "Province 1")
        self.assertEqual(self.province.region.name, "Region 1")
