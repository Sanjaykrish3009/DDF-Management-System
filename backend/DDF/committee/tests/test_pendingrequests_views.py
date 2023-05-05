from django.test import TestCase
from django.urls import reverse
from faculty.models import FacultyUser
from committee.models import CommitteeUser
from unittest.mock import patch
from request.models import FundRequest
from rest_framework import status
from django.forms.models import model_to_dict


class CommitteePendingRequestsTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.user = CommitteeUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status="Pending", hod_approval_status="Pending")
        self.fundrequest.save()
        self.request_dict = model_to_dict(self.fundrequest,exclude=['upload'])
        self.url = reverse('committee:pendingrequests')

    @patch('committee.models.CommitteeUser.view_pending_requests')
    @patch('committee.models.CommitteeUser.objects.filter')    
    def test_view_pending_requests(self,mock_committee_object,mock_committee_pending_requests):
        self.client.login(email='test@gmail.com', password='testpassword')
        mock_committee_object.return_value = [self.user]
        mock_committee_pending_requests.return_value = [self.request_dict]
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Pending requests of committee retrieved successfully')
        self.assertEqual(response.data['data'],[self.request_dict])
        self.client.logout()
   
    def test_view_pending_requests_failed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    @patch('committee.models.CommitteeUser.search_view_pending_requests')
    @patch('committee.models.CommitteeUser.objects.filter')    
    def test_view_pending_requests_search(self,mock_committee_object,mock_committee_search_pending_requests):
        self.client.login(email='test@gmail.com', password='testpassword')
        data={'title':'Test'}
        mock_committee_object.return_value = [self.user]
        mock_committee_search_pending_requests.return_value = [self.request_dict]
        response = self.client.get(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Pending requests of committee retrieved successfully')
        self.assertEqual(response.data['data'],[self.request_dict])
        self.client.logout()