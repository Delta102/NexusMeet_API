from django.db import models
from api.models import UserPromotor
from api_entrys.models import Entry

# Create your models here.
class Event(models.Model):
    date_event_start = models.DateTimeField()
    event_name = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=400)
    capacity = models.IntegerField()
    latitude = models.FloatField(null = True, blank = True) 
    longitude = models.FloatField(null = True, blank = True)
    entry_type = models.CharField(max_length = 200)
    entry_price = models.FloatField()

    creator = models.ForeignKey(UserPromotor, on_delete=models.CASCADE, related_name='created_events')
    attendees = models.ManyToManyField(UserPromotor, through=Entry, related_name='attending_events')

class Punctuation(models.Model):
    average_score = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(UserPromotor, on_delete=models.CASCADE)