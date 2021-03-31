from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    phone_no = PhoneNumberField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.username
    