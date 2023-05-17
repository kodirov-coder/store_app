from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="users/", null=True, blank=True)
