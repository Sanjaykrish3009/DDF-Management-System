from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from authentication.models import CustomUser


class LogoutTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.url = reverse('authentication:logout')

    def test_logout(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': 'Logout Successful'})
        self.client.logout()
    
    def test_invalid_logout(self):
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
