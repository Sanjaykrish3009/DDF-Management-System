from django.test import TestCase
from django.urls import reverse
from faculty.models import FacultyUser
from hod.models import HodUser
from unittest.mock import patch
from request.models import FundRequest
from rest_framework import status
from django.forms.models import model_to_dict


class HodPendingRequestsTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status="Approved", hod_approval_status="Pending")
        self.fundrequest.save()
        self.request_dict = model_to_dict(self.fundrequest,exclude=['upload'])
        self.url = reverse('hod:pendingrequests')

    @patch('hod.models.HodUser.view_pending_requests')
    @patch('hod.models.HodUser.objects.filter')    
    def test_view_pending_requests(self,mock_hod_object,mock_hod_pending_requests):
        self.client.login(email='test@gmail.com', password='testpassword')
        mock_hod_object.return_value = [self.user]
        mock_hod_pending_requests.return_value = [self.request_dict]
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Pending requests of hod retrieved successfully')
        self.assertEqual(response.data['data'],[self.request_dict])
        self.client.logout()
   
    def test_view_pending_requests_failed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    @patch('hod.models.HodUser.search_view_pending_requests')
    @patch('hod.models.HodUser.objects.filter')    
    def test_view_pending_requests_search(self,mock_hod_object,mock_hod_search_pending_requests):
        self.client.login(email='test@gmail.com', password='testpassword')
        data={'title':'Test'}
        mock_hod_object.return_value = [self.user]
        mock_hod_search_pending_requests.return_value = [self.request_dict]
        response = self.client.get(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Pending requests of hod retrieved successfully')
        self.assertEqual(response.data['data'],[self.request_dict])
        self.client.logout()
