from django.db import models
from django.contrib.auth.models import AbstractUser

class UserPromotor(AbstractUser):
    user_type = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)


class Event(models.Model):
    date_event_start = models.DateTimeField()
    event_name = models.CharField(max_length=200)
    name_event_image = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=400)
    protocols = models.CharField(max_length=500)
    capacity = models.IntegerField()
    entry_price = models.FloatField()

    creator = models.ForeignKey(UserPromotor, on_delete=models.CASCADE, related_name='created_events')

    def __str__(self):
        return self.event_name
