from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email)
        user.set_password(password)
        user.save(self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
   
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
    