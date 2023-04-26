from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from request.models import FundRequest
from transaction.models import Transaction
from authentication.models import CustomUser
from rest_framework import status

class TransactionDetailsTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.user.save()
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.fundrequest.save()
        self.transaction = Transaction(request = self.fundrequest, remaining_budget = 200.00)
        self.transaction.save()
        self.url = reverse('transaction:transactiondetails')

    @patch('transaction.models.Transaction.objects.get')
    @patch('transaction.models.Transaction.get_transaction_details')
    def test_transactiondetails(self, mock_get_transaction_details,mock_Transaction):
        self.client.login(email = "test@gmail.com",password='testpassword')
        mock_Transaction.return_value = self.transaction
        mock_get_transaction_details.return_value = {'id': 1, 'request': {'id': 1, 'request_amount': 11.00, 'transaction_type': 'Debit', 'user': {'email': 'test@gmail.com'}}, 'remaining_budget': 200.00}
        data = {'transaction_id':'1'}
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'Transaction viewed successfully')

    def test_transactiondetails_invalid_data(self):
        self.client.login(email = "test@gmail.com",password='testpassword')
        with self.assertRaises(ValueError):
            self.client.post(self.url)

    def test_transactiondetails_invalid_user(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


