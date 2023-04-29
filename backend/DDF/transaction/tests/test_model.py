from django.test import TestCase
from request.models import FundRequest
from transaction.models import Transaction
from authentication.models import CustomUser

class TransactionTest(TestCase):
    def setUp(self):
        self.user = CustomUser(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.transaction = Transaction(request = self.fundrequest, remaining_budget = 200.00)
    
    def test_create_transaction(self):
        self.assertEqual(self.transaction.request, self.fundrequest)
        self.assertEqual(self.transaction.remaining_budget, 200.00)
    
    def test_get_remaining_budget(self):
        remaining_budget = self.transaction.get_remaining_budget()
        self.assertEqual(remaining_budget, 200.00)

    def test_get_transaction_details(self):
        transaction_dict = self.transaction.get_transaction_details()
        self.assertEqual(transaction_dict['remaining_budget'],200.00)
        self.assertEqual(transaction_dict['request']['request_amount'], 11.00)
        self.assertEqual(transaction_dict['request']['transaction_type'], 'Debit')
        self.assertEqual(transaction_dict['request']['user']['email'], 'test@gmail.com')



