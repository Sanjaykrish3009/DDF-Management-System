from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from user.models import UserProfile
from authentication.models import CustomUser

class LoginTestCase(TestCase):
    def setUp(self):
        self.client =  APIClient()
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.url = reverse('authentication:login')
        self.user_profile = UserProfile(user = self.user, first_name = 'a', last_name = 'b', user_type = 'faculty')

    @patch('django.contrib.auth.authenticate')
    @patch('user.models.UserProfile.objects.get')
    @patch('user.models.UserProfile.get_user_type')
    def test_login(self, mock_get_user_type, mock_get_user_profile, mock_authenticate):
        data = {'email': 'test@gmail.com', 'password': 'testpassword'}
        mock_authenticate.return_value = self.user
        mock_user_profile = self.user_profile
        mock_get_user_type.return_value = 'faculty'
        mock_get_user_profile.return_value = mock_user_profile           
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'User authenticated')
        self.assertEqual(response.data['user_type'], 'faculty')
    
    @patch('django.contrib.auth.authenticate')
    def test_unsuccessful_login(self, mock_authenticate):
        data = {'email': 'test@gmail.com', 'password': 'wrongpassword'}
        mock_authenticate.return_value = self.user
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'], 'Invalid Credentials')
    
    def test_login_without_email(self):
        data = {'password': 'wrongpassword'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'], 'Email field must be set')

    def test_login_without_password(self):
        data = {'email': 'test@gmail.com'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'], 'Password field must be set')

        

