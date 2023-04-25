from django.test import TestCase
from django.urls import reverse
from authentication.models import CustomUser
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.client.login(email='test@gmail.com', password='testpassword')
        self.url = reverse('request:createpublicrequest')   

    def test_create_public_request(self):

        file_content = b'This is a test file'
        file = SimpleUploadedFile('test_file.txt', file_content)

        data = {
            'request_title': 'testing',
            'request_description': 'This is a test public request.',
            'request_amount': 100.00,
            'file': file
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': 'Public Fund Request created successfully'})
    
    def test_create_public_request_invalid(self):

        data = {
            'request_title': 'testing',
            'request_description': 'This is a test public request.',
            'request_amount': 100.00,
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'error': 'File must be uploaded for public request'})
