from django.test import TestCase
from request.models import FundRequest
from authentication.models import CustomUser

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
    
    def test_create_invalid_fundrequest(self):
        with self.assertRaises(ValueError):
            fundrequest = FundRequest(user=self.user, request_type='InvalidRequest', request_title='Testing', request_description='This request is created for testing', request_amount=11.00)
            fundrequest.save()

    def test_get_request_amount(self):
        request_amount = self.fundrequest.get_request_amount()
        self.assertEqual(request_amount, 11.00)
    
    def test_set_committee_approval(self):
        self.fundrequest.set_committee_approval('okay')
        self.assertEqual(self.fundrequest.committee_approval_status, 'Approved')
        self.assertEqual(self.fundrequest.committee_review, 'okay')
    
    def test_set_committee_disapproval(self):
        self.fundrequest.set_committee_disapproval('not okay')
        self.assertEqual(self.fundrequest.committee_approval_status, 'Disapproved')
        self.assertEqual(self.fundrequest.committee_review, 'not okay')

    def test_set_hod_approval_invalid(self):
        with self.assertRaises(TypeError):
            self.fundrequest.set_hod_approval()
    
    def test_set_hod_disapproval(self):
        self.fundrequest.set_hod_disapproval('not okay')
        self.assertEqual(self.fundrequest.hod_approval_status, 'Disapproved')
        self.assertEqual(self.fundrequest.hod_review, 'not okay')
    
    def test_get_request_data(self):
        request_dict = self.fundrequest.get_request_data()
        id = self.fundrequest.id
        self.assertEqual(request_dict['id'], id)
        self.assertEqual(request_dict['request_title'], 'Testing')
        self.assertEqual(request_dict['committee_approval_status'], 'Pending')
        self.assertEqual(request_dict['hod_approval_status'], 'Pending')

    def test_get_request_details(self):
        request_dict = self.fundrequest.get_request_details()
        id = self.fundrequest.id
        email = self.fundrequest.user.email
        self.assertEqual(request_dict['id'], id)
        self.assertEqual(request_dict['request_title'], 'Testing')
        self.assertEqual(request_dict['committee_approval_status'], 'Pending')
        self.assertEqual(request_dict['hod_approval_status'], 'Pending')
        self.assertEqual(request_dict['user'], {'email':email})