from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        """
        Valida que no falten datos obligatorios en la solicitud POST.
        """
        required_fields = ['date_event_start', 'event_name', 'description', 'capacity', 'entry_price', 'user_id']

        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            raise serializers.ValidationError({
            'error': 'Datos faltantes',
            'missing_fields': missing_fields
        })

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPromotor
        fields = '__all__'

    def validate(self, data):
        """
        Valida que no falten datos obligatorios en la solicitud POST.
        """
        required_fields = ['email', 'nombre', 'apellido', 'tipoUser']

        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            raise serializers.ValidationError({
            'error': 'Datos faltantes',
            'missing_fields': missing_fields
        })

        return data