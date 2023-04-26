from django.test import TestCase
from authentication.models import CustomUser
from hod.models import HodUser
from unittest.mock import Mock, patch
from request.models import FundRequest
from transaction.models import Transaction

class HodUserTest(TestCase):
    def setUp(self):
        self.user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, transaction_type = 'Credit')
        self.transaction = Transaction(request=self.user,)

    def test_create_hod_user(self):
        self.assertEqual(HodUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.user.email, 'test@gmail.com')
    
    @patch('request.models.FundRequest')
    @patch('transaction.models.Transaction')
    def test_approve_request_no_transactions(self, mock_transaction, mock_fund_request):
        mock_fund_request_obj = self.fundrequest
        mock_fund_request_obj.get_request_amount.return_value = 11.00
        mock_fund_request.objects.get.return_value = mock_fund_request_obj
        mock_transaction.objects.exists.return_value = False
        mock_fund_request_obj.approve_request(1, "approved")
        latest_transaction = Transaction.objects.latest('transaction_date')
        remaining_budget = latest_transaction.get_remaining_budget()
        self.assertEqual(remaining_budget, 0.00)