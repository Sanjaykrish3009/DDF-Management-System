from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from faculty.models import FacultyUser
from user.models import UserProfile
from django.urls import reverse
from rest_framework import status

class SignupTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = FacultyUser.objects.create_user(email='faculty@gmail.com',password='faculty')
        self.userprofile = UserProfile(user=self.user,first_name='facultyname',last_name='cse',user_type='faculty')
        self.url = reverse('user:signup')
  
    @patch('user.models.UserProfile')
    @patch('faculty.models.FacultyUser.objects.create_user')
    @patch('faculty.models.FacultyUser.objects.filter')
    def test_signup(self,mock_user_already_exists,mock_create_user,mocK_create_userprofile):
        data= {'first_name':'facultyname','last_name':'cse','email':'facuty@gmail.com','password':'faculty123','re_password':'faculty123'}
        mock_user_already_exists.return_value.exists.return_value = False
        mock_create_user.return_value = self.user
        mocK_create_userprofile.return_value = self.userprofile
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'],'OTP sent for email verification')

    @patch('authentication.models.CustomUser.objects.filter')
    def test_unsuccessful_signup(self,mock_user_already_exists):
        data= {'first_name':'facultyname','last_name':'cse','email':'facuty@gmail.com','password':'faculty123','re_password':'faculty123'}
        mock_user_already_exists.return_value.exists.return_value = True
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'],'email already exists')


    @patch('faculty.models.FacultyUser.objects.filter')
    def test_unsuccessful_signup_password(self,mock_user_already_exists):
        data= {'first_name':'facultyname','last_name':'cse','email':'facuty@gmail.com','password':'cse12','re_password':'cse12'}
        mock_user_already_exists.return_value.exists.return_value = False
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'],'Password must be atleast 6 characters')       

    def test_signup_without_email(self):
        data= {'first_name':'facultyname','last_name':'cse','password':'faculty123','re_password':'faculty123'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'],'Email field must be set')       
        