from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from faculty.models import FacultyUser
from user.models import UserProfile
from django.urls import reverse
from rest_framework import status

class ChangePasswordTestCase(TestCase):
    def setUp(self):
        self.user = FacultyUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.url = reverse('user:changepassword')

    def test_successful_changepassword(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'old_password':'testpassword','new_password':'testingpassword','re_new_password':'testingpassword'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'],'Password Changed successfully')

    def test_changepassword_without_oldpassword(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'re_new_password':'testingpassword'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'],'Old Password field must be set')
        
    def test_changepassword_invalid_password(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'old_password':'testpass','new_password':'tesingpassword','re_new_password':'testingpassword'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'],'Incorrect Old Password')
        self.client.logout()

    def test_changepassword_invalid_confirmpassword(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'old_password':'testpassword','new_password':'tesingpassword','re_new_password':'testing1password'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'],'Passwords do not match')
        self.client.logout()
