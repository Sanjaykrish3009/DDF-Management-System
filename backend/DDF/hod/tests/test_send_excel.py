from django.test import TestCase
from django.urls import reverse
from hod.models import HodUser
from unittest.mock import patch
from rest_framework import status

class HodSendExcelTest(TestCase):
    def setUp(self):
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.url = reverse('hod:sendexcelsheet')

    @patch('hod.models.HodUser.send_excel')
    def test_send_excel_success(self, mock_send_excel):
        self.client.login(email='test@gmail.com', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': 'Excel Sheet sent to admin'})
        mock_send_excel.assert_called_once()

    @patch('hod.models.HodUser.send_excel')
    def test_send_excel_error(self, mock_send_excel):
        self.client.login(email='test@gmail.com', password='testpassword')
        mock_send_excel.side_effect = Exception('test_exception')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'error': 'Something went wrong while sending excel sheet to admin'})
        mock_send_excel.assert_called_once()

    def test_send_excel_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
