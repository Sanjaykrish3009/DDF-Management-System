from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from transaction.models import Transaction
from request.models import FundRequest
from committee.models import CommitteeUser

class Approval(TestCase):
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
        self.url = reverse('committee:approve')

    @patch('committee.models.CommitteeUser.objects.get')
    @patch('committee.models.CommitteeUser.approve_request')

    def test_approval(self,mock_approve_request,mock_getobject):
        self.client.login(email='test@gmail.com', password='testpassword')
        data = {'request_id':'1', 'committee_review':'Approved'}
        mock_getobject.return_value = self.Comittee_user
        mock_approve_request.return_value =  self.transaction
        response = self.client.post(self.url,data)
        print(response.data)
        self.assertEqual(response.data['success'],'Fund request disapproved by the committee successfully')
