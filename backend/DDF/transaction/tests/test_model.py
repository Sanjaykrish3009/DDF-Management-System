from django.test import TestCase
from request.models import FundRequest
from transaction.models import Transaction
from authentication.models import CustomUser
from django.utils import timezone


class TransactionTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.user.save()
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.fundrequest.save()
        self.transaction = Transaction(request = self.fundrequest, remaining_budget = 200.00)
        self.transaction.save()
    
    def test_create_transaction(self):
        self.assertEqual(self.transaction.request, self.fundrequest)
        self.assertEqual(self.transaction.remaining_budget, 200.00)
    
    def test_get_remaining_budget(self):
        remaining_budget = self.transaction.get_remaining_budget()
        self.assertEqual(remaining_budget, 200.00)

    # def test_get_transaction_details(self):
    #     date = timezone.localtime(self.transaction.transaction_date).strftime('%Y-%m-%d %H:%M:%S')
    #     transaction_dict = self.transaction.get_transaction_details()
    #     expected_dict = {'id': 1, 'request': {'id': 1, 'request_amount': 11.00, 'transaction_type': 'Debit', 'user': {'email': 'test@gmail.com'}}, 'remaining_budget': 200.00, 'transaction_date': date}
    #     self.assertEqual(transaction_dict,expected_dict)
        