from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from faculty.models import FacultyUser
from user.models import UserProfile
from django.urls import reverse
from rest_framework import status


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.user = FacultyUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.userprofile = UserProfile(user=self.user,first_name='firstname',last_name='lastname',user_type='faculty')
        self.url = reverse('user:viewprofile')

    @patch('user.models.UserProfile.get_user_profile')
    @patch('user.models.UserProfile.objects.get')
    def test_succesful_viewprofile(self,mock_user,mock_get_userprofile):
        self.client.login(email='test@gmail.com', password='testpassword') 
        mock_user.return_value = self.userprofile
        mock_get_userprofile.return_value = {'firstname':'firstname','lastname':'lastname','email':'test@gmail.com'}
       
        response = self.client.get(self.url,format='json')        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'],'Profile retrieved Succesfully')
        self.assertEqual(response.data['profile'],self.userprofile.get_user_profile())
        self.client.logout()

    @patch('user.models.UserProfile.get_user_profile')
    @patch('user.models.UserProfile.objects.get')
    def test_unsuccesful_viewprofile_without_login(self,mock_user,mock_get_userprofile):
        mock_user.return_value = self.userprofile
        mock_get_userprofile.return_value = {'firstname':'firstname','lastname':'lastname','email':'test@gmail.com'}
       
        response = self.client.get(self.url,format='json')        
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)     

