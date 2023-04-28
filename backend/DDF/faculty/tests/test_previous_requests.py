from django.test import TestCase
from django.urls import reverse
from faculty.models import FacultyUser
from unittest.mock import patch
from request.models import FundRequest
from rest_framework import status
from django.forms.models import model_to_dict

class FacultyPendingRequestsTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status = "Approved", hod_approval_status="Approved")
        self.fundrequest.save()
        
        self.request_dict = model_to_dict(self.fundrequest,exclude=['upload'])
        self.url = reverse('faculty:previousrequests')

    @patch('faculty.models.FacultyUser.view_previous_requests')
    @patch('faculty.models.FacultyUser.objects.filter')    
    def test_view_pending_requests(self,mock_faculty_object,mock_faculty_previous_requests):
        self.client.login(email='testing@gmail.com', password='testingpassword')
        mock_faculty_object.return_value = [self.faculty_user]
        mock_faculty_previous_requests.return_value = [self.request_dict]
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Previous requests of faculty retrieved successfully')
        self.assertEqual(response.data['data'],[self.request_dict])
        self.client.logout()
   
    def test_view_previous_requests_failed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_previous_requests_failed_login(self):
        self.client.login(email='test@gmail.com', password='testingpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'],'Authentication credentials were not provided.')


    @patch('faculty.models.FacultyUser.search_view_previous_requests')
    @patch('faculty.models.FacultyUser.objects.filter')    
    def test_view_previous_requests_search(self,mock_faculty_object,mock_faculty_search_pending_requests):
        self.client.login(email='testing@gmail.com', password='testingpassword')
        data={'title':'Test'}
        mock_faculty_object.return_value = [self.faculty_user]
        mock_faculty_search_pending_requests.return_value = [self.request_dict]
        response = self.client.get(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Previous requests of faculty retrieved successfully')
        self.assertEqual(response.data['data'],[self.request_dict])
        self.client.logout()