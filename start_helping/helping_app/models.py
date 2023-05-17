from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(email=self.normalize_email(email))
#
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password):
#         user = self.create_user(email, password=password)
#         user.is_admin = True
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user
#

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email


