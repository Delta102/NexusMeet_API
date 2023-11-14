from django.db import models
from api.models import UserPromotor

# Create your models here.
class Entry(models.Model):
    quantity = models.IntegerField()
    price_total = models.FloatField()
    image_qr = models.ImageField(upload_to = 'entry_qr_codes', blank = True, null = True)
    event = models.ForeignKey('api_events.Event', on_delete=models.CASCADE, related_name = 'entries')
    event_name = models.CharField(max_length = 200, null = True, blank = True)
    user_id = models.ForeignKey(UserPromotor, on_delete=models.CASCADE)