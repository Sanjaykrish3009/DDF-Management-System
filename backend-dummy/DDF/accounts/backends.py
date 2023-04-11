from django.contrib.auth.backends import ModelBackend, UserModel
from accounts.models import FacultyUser, CommitteeUser, HodUser

class FacultyUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = FacultyUser.objects.get(email=email)
        except FacultyUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None

class CommitteeUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CommitteeUser.objects.get(email=email)
        except CommitteeUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None

class HodUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = HodUser.objects.get(email=email)
        except HodUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None
