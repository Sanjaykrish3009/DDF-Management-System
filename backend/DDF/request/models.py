from django.db import models
from authentication.models import CustomUser
from django.utils import timezone
from django.forms.models import model_to_dict


class FundRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('PublicRequest', 'Public Request'),
        ('PrivateRequest', 'Private Request'),
    ]
    REQUEST_STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Disapproved', 'Disapproved'),
        ('Pending', 'Pending'),
    ]
    TRANSACTION_TYPE_CHOICES = [
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    request_title = models.CharField(max_length=300)
    request_description = models.CharField(max_length=3000)
    request_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES,default='Debit')
    request_date = models.DateTimeField(auto_now_add=True)
    committee_approval_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='Pending')
    hod_approval_status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='Pending')
    committee_review = models.CharField(max_length=3000, blank=True, null=True)
    committee_review_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    hod_review = models.CharField(max_length=3000, blank=True, null=True)
    hod_review_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    upload = models.FileField(upload_to = '', default='')

    def get_request_amount(self):
        return self.request_amount

    def set_committee_approval(self, committee_review):
        self.committee_approval_status = 'Approved'
        self.committee_review = committee_review
        self.committee_review_date = timezone.now()
        self.save()

    def set_committee_disapproval(self, committee_review):
        self.committee_approval_status = 'Disapproved'
        self.committee_review = committee_review
        self.committee_review_date = timezone.now()
        self.save()

    def set_hod_approval(self, hod_review):
        self.hod_approval_status = 'Approved'
        self.hod_review = hod_review
        self.hod_review_date = timezone.now()
        self.save()

    def set_hod_disapproval(self, hod_review):
        self.hod_approval_status = 'Disapproved'
        self.hod_review = hod_review
        self.hod_review_date = timezone.now()
        self.save()

    def get_request_details(self):    
        if self.upload != '':
            request_dict = model_to_dict(self)
            request_dict['upload'] = request_dict['upload'].name
        else:
            request_dict = model_to_dict(self, exclude=['upload'])

    
        request_dict['user'] = model_to_dict(self.user, fields=['email'])
        request_dict['request_date'] = timezone.localtime(self.request_date).strftime('%Y-%m-%d %H:%M:%S')
        request_dict['committee_review_date'] = timezone.localtime(self.committee_review_date).strftime('%Y-%m-%d %H:%M:%S')
        request_dict['hod_review_date'] = timezone.localtime(self.hod_review_date).strftime('%Y-%m-%d %H:%M:%S')

        return request_dict
    
    def get_request_data(self):
        request_dict = model_to_dict(self, fields=['id', 'request_title', 'committee_approval_status', 'hod_approval_status'])    
        request_dict['request_date'] = timezone.localtime(self.request_date).strftime('%Y-%m-%d %H:%M:%S')   
        return request_dict
    
    def get_transaction_type(self):
        return self.transaction_type
       