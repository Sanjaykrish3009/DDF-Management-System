from django.db import models
from authentication.models import CustomUser

class FacultyUser(CustomUser):
    faculty_id = models.CharField(max_length=30)