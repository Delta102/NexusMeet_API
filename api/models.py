from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
#class UserPromotor(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    phone_number = models.CharField(max_length=9)
#    name = models.CharField(max_length= 200)
#    last_name = models.CharField(max_length= 200)
#    user_type = models.CharField(max_length= 8)

class Event(models.Model):
    date_event_start = models.DateTimeField()
    event_name = models.CharField(max_length= 200)
    name_event_image = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length= 400)
    protocols = models.CharField(max_length= 500)
    capacity = models.IntegerField()
    entry_price = models.FloatField()
    user_id = models.IntegerField() ## SIMULACIÓN DEL USER ID
#    user = models.ForeignKey(UserPromotor, on_delete=models.CASCADE)

