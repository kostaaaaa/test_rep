from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class UserInfo(models.Model):
    get_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='get_user', unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    address = models.CharField(max_length=100)
