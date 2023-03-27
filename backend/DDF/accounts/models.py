from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(self._db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class FacultyUser(CustomUser):
    faculty_id = models.CharField(max_length=30)
    
class CommitteeUser(CustomUser):
    committee_id = models.CharField(max_length=30)

class HodUser(CustomUser):
    hod_id = models.CharField(max_length=30)

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

class Transaction(models.Model):
    request = models.ForeignKey(FundRequest, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    remaining_budget = models.DecimalField(max_digits=10, decimal_places=2)
