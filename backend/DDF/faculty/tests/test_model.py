from django.test import TestCase
from authentication.models import CustomUser
from hod.models import HodUser
from unittest.mock import patch
from request.models import FundRequest
from transaction.models import Transaction
from faculty.models import FacultyUser
from request.viewrequests.pendingrequest_strategy import PendingRequestStrategy
from django.forms.models import model_to_dict


class FacultyUserTest(TestCase):
    def setUp(self):
        self.faculty_user = FacultyUser.objects.create_user(email='testing@gmail.com', password='testingpassword')
        self.pending_strategy = PendingRequestStrategy()
        self.fundrequest = FundRequest(user=self.faculty_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.fundrequest.save()
        self.request_dict = model_to_dict(self.fundrequest,exclude=['upload'])
        self.request_dict['request_date'] = '2022-01-01 00:00:00'


    def test_create_facuty_user(self):
        self.assertEqual(FacultyUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.faculty_user.email, 'testing@gmail.com')
        self.assertTrue(self.faculty_user.check_password('testingpassword'))

    @patch('faculty.models.FacultyUser.fetch_requests_data')
    @patch('request.viewrequests.pendingrequest_strategy.PendingRequestStrategy.view_requests')
    def test_view_pending_requests(self,mock_pending_requests_strategy,mock_requests_data):
        self.client.login(email='testing@gmail.com', password='testingpassword')
        mock_pending_requests_strategy.return_value = [self.fundrequest]
        mock_requests_data.return_value = [self.request_dict]
        pendingrequests = self.faculty_user.view_pending_requests()
        self.assertEqual(pendingrequests,[self.request_dict])


    @patch('request.models.FundRequest.get_request_data')
    def test_fetch_requests_data(self,mock_get_request_data):
        mock_get_request_data.return_value=self.request_dict
        data_list = self.faculty_user.fetch_requests_data([self.fundrequest])
        self.assertEqual(data_list,[self.request_dict])



