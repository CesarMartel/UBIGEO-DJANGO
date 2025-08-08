from django.test import TestCase
from province.models import Province, Region, User, Patient, Therapist, District

class ProvinceModelTest(TestCase):

    def setUp(self):
        # Set up los modelos necesarios para las pruebas
        self.region = Region.objects.create(name="Region 1")
        self.province = Province.objects.create(name="Province 1", region=self.region)

        # Crear instancias de los otros modelos
        self.user = User.objects.create(username="user1")
        self.patient = Patient.objects.create(name="Patient 1")
        self.therapist = Therapist.objects.create(name="Therapist 1")
        self.district = District.objects.create(name="District 1")

        # Establecer relaciones ManyToMany
        self.province.users.add(self.user)
        self.province.patients.add(self.patient)
        self.province.therapists.add(self.therapist)
        self.province.districts.add(self.district)

    def test_province_creation(self):
        # Verifica que la provincia se haya creado correctamente
        self.assertEqual(self.province.name, "Province 1")
        self.assertEqual(self.province.region.name, "Region 1")

    def test_province_relation_with_user(self):
        # Verifica la relación ManyToMany con el modelo User
        self.assertIn(self.user, self.province.users.all())

    def test_province_relation_with_patient(self):
        # Verifica la relación ManyToMany con el modelo Patient
        self.assertIn(self.patient, self.province.patients.all())

    def test_province_relation_with_therapist(self):
        # Verifica la relación ManyToMany con el modelo Therapist
        self.assertIn(self.therapist, self.province.therapists.all())

    def test_province_relation_with_district(self):
        # Verifica la relación ManyToMany con el modelo District
        self.assertIn(self.district, self.province.districts.all())

    def test_str_method(self):
        # Verifica que el método __str__ devuelva el nombre de la provincia
        self.assertEqual(str(self.province), "Province 1")
