from django.test import TestCase
from authentication.models import CustomUser
from hod.models import HodUser
from unittest.mock import patch
from request.models import FundRequest
from transaction.models import Transaction
from faculty.models import FacultyUser

class HodUserTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.hod_user = HodUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status="Approved", hod_approval_status="Pending")
        self.fundrequest.save()
        self.approvedfundrequest = FundRequest(user=self.hod_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status = "Approved", hod_approval_status="Approved")
        self.approvedfundrequest.save()
        self.latest_fundrequest =  FundRequest(user=self.hod_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=111.00, transaction_type = 'Credit')
        self.latest_fundrequest.save()
        self.latest_transaction = Transaction(request=self.approvedfundrequest, remaining_budget=111.00)
        self.latest_fundrequest.save()
        self.transaction = Transaction(request=self.fundrequest, remaining_budget=100.00)
        self.transaction.save()

    def test_create_hod_user(self):
        self.assertEqual(HodUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(self.hod_user.email, 'test@gmail.com')
        self.assertTrue(self.hod_user.check_password('testpassword'))
    
    @patch('request.models.FundRequest.objects.get')
    @patch('request.models.FundRequest.get_request_amount')
    @patch('request.models.FundRequest.get_transaction_type')
    @patch('hod.models.HodUser.view_balance')
    @patch('request.models.FundRequest.set_hod_approval')
    @patch('transaction.models.Transaction')
    def test_approve_request_no_transactions(self, mock_transaction_obj,mock_set_hod_approval, mock_view_balance, mock_get_transaction_type, mock_get_request_amount, mock_fundrequest_objects_get):
        mock_fundrequest_objects_get.return_value = self.fundrequest
        mock_get_request_amount.return_value = 11.00
        mock_get_transaction_type.return_value = "Debit"
        mock_view_balance.return_value = 111.00
        mock_set_hod_approval.return_value = True
        mock_transaction_obj.return_value = self.transaction
        new_transaction = self.hod_user.approve_request(1, 'approved')
        self.assertEqual(Transaction.objects.count(), 2)
        self.assertEqual(new_transaction.request, self.transaction.request)
        self.assertEqual(new_transaction.remaining_budget,self.transaction.remaining_budget)

    def test_disapprove_request_invalid(self):
        with self.assertRaises(TypeError):
            self.fundrequest.set_hod_disapproval()

    @patch('transaction.models.Transaction.objects.exists')
    @patch('transaction.models.Transaction.objects.latest')
    @patch('transaction.models.Transaction.get_remaining_budget')
    def test_view_balance(self,mock_get_remaining_budget,mock_latest,mock_transaction_object):
        mock_transaction_object.return_value = True
        mock_latest.return_value = self.latest_transaction
        mock_get_remaining_budget.return_value = 111.00
        balance = self.hod_user.view_balance()
        self.assertEqual(balance,111.00)
   
    @patch('request.models.FundRequest.objects.exclude')
    @patch('request.models.FundRequest.objects.filter')
    def test_search_view_previous_requests_invalid(self,mock_filter,mock_exclude):
        mock_exclude.return_value = [self.approvedfundrequest]
        mock_filter.return_value = [self.fundrequest]
        with self.assertRaises(TypeError):
            self.hod_user.search_view_previous_requests()
