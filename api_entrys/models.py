from django.db import models
from api.models import UserPromotor

# Create your models here.
class Entry(models.Model):
    quantity = models.IntegerField()
    price_total = models.FloatField()
    image_qr = models.ImageField(upload_to = 'entry_qr_codes', blank = True, null = True)
    event = models.ForeignKey('api_events.Event', on_delete=models.CASCADE, related_name = 'entries')
    user = models.ForeignKey(UserPromotor, on_delete=models.CASCADE)