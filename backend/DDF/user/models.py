from django.db import models
from authentication.models import CustomUser
import json

class UserProfile(models.Model):

    USER_TYPE_CHOICES = [
        ('Faculty', 'faculty'),
        ('Committee', 'committee'),
        ('Hod', 'hod')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)


    def get_user_profile(self):
        profile = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.user.email
        }

        return profile
    
    def get_user_type(self):
        return self.user_type
    