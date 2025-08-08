from django.test import TestCase
from mi_app.models import Province, District

class DistrictModelTest(TestCase):
    def setUp(self):
        self.province = Province.objects.create(name="Lima")
        self.district = District.objects.create(name="Miraflores", province=self.province)

    def test_district_creation(self):
        self.assertEqual(self.district.name, "Miraflores")
        self.assertEqual(self.district.province.name, "Lima")

    def test_str_method(self):
        self.assertEqual(str(self.district), "Miraflores")
