from rest_framework import serializers
from .models import *

class UserPromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPromotor
        fields = '__all__'