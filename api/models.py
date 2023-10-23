from django.db import models
from django.contrib.auth.models import AbstractUser

class UserPromotor(AbstractUser):
    user_type = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)