from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faculty.models import FacultyUser
from committee.models import CommitteeUser
from hod.models import HodUser
from unittest.mock import patch
from request.models import FundRequest
from transaction.models import Transaction
from rest_framework import status


class HodUserApprovalTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status="Approved", hod_approval_status="Pending")
        self.fundrequest.save()
        self.transaction = Transaction(request=self.fundrequest, remaining_budget=100.00)
        self.transaction.save()
        self.url = reverse('hod:approve')

    @patch('hod.models.HodUser.approve_request')
    @patch('hod.models.HodUser.objects.filter')
    def test_approval(self,mock_hod_object,mock_hod_approve_request):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'request_id':self.fundrequest.id, 'hod_review':'Approving'}
        mock_hod_object.return_value = [self.user]
        mock_hod_approve_request.return_value = self.transaction
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Fund request approved by the hod successfully')
        self.client.logout()


    @patch('hod.models.HodUser.approve_request')
    @patch('hod.models.HodUser.objects.filter')   
    def test_approval_failed(self,mock_hod_object,mock_hod_approve_request):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'request_id':self.fundrequest.id, 'hod_review':'Approving'}
        mock_hod_object.return_value = [self.user]
        mock_hod_approve_request.return_value = None
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'], 'Request amount more than remaining budget')
        self.client.logout()

    def test_approval_failed_without_request(self):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'hod_review':'Approving'}
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['error'], 'Request ID field must be set')


