from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class RegionViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('regions')

    def test_get_regions(self):
        """Verifica que el endpoint GET /regions/ funciona"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'GET regiones')

    def test_post_region(self):
        """Verifica que el endpoint POST /regions/ funciona"""
        data = {'name': 'Lima'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'POST región')
