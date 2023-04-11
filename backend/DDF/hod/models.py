from django.db import models
from authentication.models import CustomUser

class HodUser(CustomUser):
    hod_id = models.CharField(max_length=30)