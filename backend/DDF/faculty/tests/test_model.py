from django.test import TestCase
from request.models import FundRequest
from authentication.models import CustomUser
from django.utils import timezone


class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.fundrequest = FundRequest(user=self.user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)

    def test_create_fundrequest(self):
        self.assertEqual(self.fundrequest.user, self.user)
        self.assertEqual(self.fundrequest.request_type, 'PrivateRequest')
        self.assertEqual(self.fundrequest.request_title, 'Testing')
        self.assertEqual(self.fundrequest.request_description, 'This request is created for testing')
        self.assertEqual(self.fundrequest.request_amount, 11.00)

   