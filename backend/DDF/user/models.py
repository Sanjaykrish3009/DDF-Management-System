from django.db import models
from authentication.models import CustomUser

class UserProfile(models.Model):

    USER_TYPE_CHOICES = [
        ('Faculty', 'faculty'),
        ('Committee', 'committee'),
        ('Hod', 'hod')
    ]

    _user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    _first_name = models.CharField(max_length=20)
    _last_name = models.CharField(max_length=20)
    _user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    