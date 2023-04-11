from django.db import models
from authentication.models import CustomUser

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
    upload = models.FileField(upload_to ='uploads/')