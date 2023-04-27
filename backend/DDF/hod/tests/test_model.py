from django.test import TestCase
from authentication.models import CustomUser
from hod.models import HodUser
from unittest.mock import patch
from request.models import FundRequest
from transaction.models import Transaction

class HodUserTest(TestCase):
    def setUp(self):
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.latest_fundrequest =  FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=111.00, transaction_type = 'Credit')
        self.transaction = Transaction(request=self.fundrequest, remaining_budget=100.00)
        self.latest_transaction = Transaction(request=self.latest_fundrequest, remaining_budget=111.00)

    def test_create_hod_user(self):
        self.assertEqual(HodUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertTrue(self.user.check_password('testpassword'))
    
    @patch('request.models.FundRequest.objects.get')
    @patch('request.models.FundRequest.get_request_amount')
    @patch('transaction.models.Transaction.objects')
    @patch('transaction.models.Transaction.objects.latest')
    @patch('transaction.models.Transaction.get_remaining_budget')
    @patch('request.models.FundRequest.set_hod_approval')
    def test_approve_request_no_transactions(self, mock_set_hod_approval, mock_get_remaining_budget, mock_latest_transaction, mock_transaction, mock_get_request_amount, mock_fundrequest_objects_get):
        mock_fundrequest_objects_get.return_value = self.fundrequest
        mock_get_request_amount.return_value = self.fundrequest.request_amount
        mock_transaction.return_value.exists_return_value = True
        mock_latest_transaction.return_value = self.latest_transaction
        mock_get_remaining_budget.return_value = self.latest_transaction.remaining_budget
        mock_set_hod_approval.return_value = True
        transaction_obj = self.user.approve_request(1, 'approved')
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(transaction_obj, self.transaction)
