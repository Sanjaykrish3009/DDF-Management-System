from django.test import TestCase
from django.urls import reverse
from hod.models import HodUser
from unittest.mock import patch
from request.models import FundRequest
from transaction.models import Transaction
from rest_framework.test import APIClient


class HodUserTest(TestCase):
    def setUp(self):
        self.client = APIClient
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.fundrequest.save()
        self.latest_fundrequest =  FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=111.00, transaction_type = 'Credit')
        self.latest_fundrequest.save()
        self.transaction = Transaction(request=self.fundrequest, remaining_budget=100.00)
        self.transaction.save()
        self.latest_transaction = Transaction(request=self.latest_fundrequest, remaining_budget=111.00)
        self.latest_transaction.save()
        self.url = reverse('hod:pendingrequests')

    # @patch('hod.models.HodUser.view_previous_requests')
    # @patch('hod.models.HodUser.objects.get')
    # def test_pending_requests(self, mock_hod_object_get, mock_view_pending_requests):
    #     self.data = {'user': self.user, 'email': 'test@gmail.com'}
    #     mock_hod_object_get.return_value = self.user
    #     mock_view_pending_requests.return_value = 

