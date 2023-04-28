from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from transaction.models import Transaction
from request.models import FundRequest
from committee.models import CommitteeUser
# from rest_framework.test import APIClient

class PendingRequestsTest(TestCase):
    def setUp(self):
        self.Comittee_user = CommitteeUser.objects.create_user(email = 'test@gmail.com',password ='testpassword')
        self.fundrequest = FundRequest(user=self.Comittee_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
        self.fundrequest.save()
        self.approvedfundrequest = FundRequest(user=self.Comittee_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00, committee_approval_status = "Approved")
        self.approvedfundrequest.save()
        self.latest_fundrequest =  FundRequest(user=self.Comittee_user, request_type='PrivateRequest', request_title='Testing', request_description='This request is created for testing', request_amount=111.00, transaction_type = 'Credit')
        self.latest_fundrequest.save()
        self.transaction = Transaction(request=self.fundrequest, remaining_budget=100.00)
        self.transaction.save()
        self.latest_transaction = Transaction(request=self.latest_fundrequest, remaining_budget=111.00)
        self.latest_transaction.save()
        self.url = reverse('committee:pendingrequests')

    @patch('committee.models.CommitteeUser.objects.get')
    @patch('committee.models.CommitteeUser.search_view_pending_requests')
    @patch('committee.models.CommitteeUser.view_pending_requests')

    def test_pending_requests(self,mock_view_pending_requests,mock_search_view_pending_requests,mock_get_committee_object):
        self.data = {'title':'Test'}
        mock_get_committee_object.return_value = self.Comittee_user
        mock_search_view_pending_requests.return_value = [{self.fundrequest}]
        mock_view_pending_requests.return_value = [{self.fundrequest}]
        self.client.login(email='test@gmail.com',password='testpassword')
        response = self.client.get(self.url,self.data,format = 'json')
        self.assertEqual(response.data['success'],'Pending requests of committee retrieved successfully')


        