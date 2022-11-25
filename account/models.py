from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from account.managers import TrainUserManager


# Create your models here.


class TrainUser(AbstractUser, PermissionsMixin):
    
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = TrainUserManager()

    def __str__(self) -> str:
        return self.email

