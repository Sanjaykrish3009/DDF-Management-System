from django.db import models
from authentication.models import CustomUser

class CommitteeUser(CustomUser):
    committee_id = models.CharField(max_length=30)