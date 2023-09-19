from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserPromotor(AbstractBaseUser):
    user_type = models.CharField(max_length=10)

    # Campos personalizados
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Campos heredados de AbstractUser
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Event(models.Model):
    date_event_start = models.DateTimeField()
    event_name = models.CharField(max_length=200)
    name_event_image = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=400)
    protocols = models.CharField(max_length=500)
    capacity = models.IntegerField()
    entry_price = models.FloatField()

    # Agrega una relación ForeignKey a UserPromotor para representar que un usuario crea el evento.
    creator = models.ForeignKey(UserPromotor, on_delete=models.CASCADE, related_name='created_events')

    def __str__(self):
        return self.event_name
