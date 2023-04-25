from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class GetCSRFTokenTestCase(TestCase):
    def setUp(self):
        self.url = reverse('authentication:getcsrftoken')

    def test_get_csrf_token(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
   
   