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
from django.forms.models import model_to_dict



class HodDebitTransactionsTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status="Approved", hod_approval_status="Approved")
        self.fundrequest.save()
        self.request_dict = model_to_dict(self.fundrequest,exclude=['upload'])
        self.transaction = Transaction(request=self.fundrequest,remaining_budget=11.00)
        self.transaction.save()
        self.transaction_dict = model_to_dict(self.transaction)
        self.transaction_dict['request']=self.request_dict
        self.url = reverse('hod:debittransactions')

    @patch('hod.models.HodUser.view_debit_transactions')
    @patch('hod.models.HodUser.objects.filter')    
    def test_view_debit_transactions(self,mock_hod_object,mock_hod_debit_transactions):
        self.client.login(email='test@gmail.com', password='testpassword')
        mock_hod_object.return_value = [self.user]
        mock_hod_debit_transactions.return_value = [self.transaction_dict]
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Debit transactions retrieved successfully by the hod')
        self.assertEqual(response.data['data'],[self.transaction_dict])
        self.client.logout()
   
    def test_view_debit_transactions_failed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

