from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from user.models import UserProfile
from authentication.models import CustomUser

class CheckauthenticationTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.url = reverse('authentication:checkauthentication')
        self.user_profile = UserProfile(user = self.user, first_name = 'a', last_name = 'b', user_type = 'faculty')

    @patch('user.models.UserProfile.objects.get')
    @patch('user.models.UserProfile.get_user_type')
    def test_success_authentication(self, mock_get_user_type, mock_get_user_profile):
        self.client.login(email='test@gmail.com', password='testpassword') 
        mock_user_profile = self.user_profile
        mock_get_user_type.return_value = 'faculty'
        mock_get_user_profile.return_value = mock_user_profile          
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['isAuthenticated'],'success')
        self.assertEqual(response.data['type'],'faculty')
        self.client.logout()
    
    @patch('user.models.UserProfile.objects.get')
    @patch('user.models.UserProfile.get_user_type')
    def test_fail_authentication(self, mock_get_user_type, mock_get_user_profile):
        mock_user_profile = self.user_profile
        mock_get_user_type.return_value = 'faculty'
        mock_get_user_profile.return_value = mock_user_profile           
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
   