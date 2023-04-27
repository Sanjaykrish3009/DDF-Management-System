# from unittest.mock import patch
from unittest.mock import patch
from django.test import TestCase
from authentication.models import CustomUser
from request.models import FundRequest
from faculty.models import FacultyUser
from request.viewrequests.pendingrequest_strategy import PendingRequestStrategy


class FacultyUserTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email = 'test@gmail.com',password ='testpassword')
        self.fundrequest1 = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.fundrequest2 =  FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=111.00, transaction_type = 'Credit')
        self.PendingRequeststrategy = PendingRequestStrategy()

    def test_faculty_user_model(self):
        self.assertEqual(FacultyUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.faculty_user.email, 'test@gmail.com')
        self.assertTrue(self.faculty_user.check_password('testpassword'))

    @patch('request.viewrequests.previousrequest_strategy.PendingRequestStrategy()')
    @patch('request.viewrequests.previousrequest_strategy.PendingRequestStrategy.view_request()')
    def test_view_pending_requests(self, mock_view_requests,mock_pendingrequests):
        mock_pendingrequests.return_value = self.PendingRequeststrategy
        mock_view_requests.return_value = [self.fundrequest1,self.fundrequest2]
        pending_requests = self.faculty_user.view_pending_requests()
        self.assertEqual(pending_requests,[self.fundrequest1,self.fundrequest2])



