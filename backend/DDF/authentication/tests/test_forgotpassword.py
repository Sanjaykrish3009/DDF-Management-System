from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from authentication.models import CustomUser

class ForgotPasswordTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.url = reverse('authentication:forgotpassword')

    @patch('authentication.models.CustomUser.objects.get')
    def test_forgot_password(self, mock_get_user):
        data = {'email': 'test@gmail.com'}
        mock_get_user.return_value = self.user  
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'OTP sent to Registered Email')
    
    @patch('authentication.models.CustomUser.objects.get')
    def test_invalid_forgot_password(self, mock_get_user):
        data = {'email': 'testinvalid@gmail.com'}
        mock_get_user.side_effect = CustomUser.DoesNotExist
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'], 'User doesnot exist with given email')
