from django.test import TestCase
from django.urls import reverse
from authentication.models import CustomUser
from rest_framework import status

class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.client.login(email='test@gmail.com', password='testpassword')
        self.url = reverse('request:createbudgetrequest')   

    def test_create_budget_request(self):
        data = {
            'request_title': 'testing',
            'request_description': 'This is a test budget request.',
            'request_amount': 100.00,
            'file': 'test_file.pdf',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': 'Budget Request created successfully'})
    
    def test_create_budget_request_invalid(self):

        data = {
            'request_title': 'testing',
            'request_description': 'This is a test private request.',
            'file': 'test_file.pdf',
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'error': 'Request Amount field must be set'})
