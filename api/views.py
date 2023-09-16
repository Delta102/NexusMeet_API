from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status

#from api import User

# Create your views here.
# @api_view(['POST'])
#@authentication_classes([])
#def create_users(request):
#    name = request.data.get('name')
#    last_name = request.data.get('last_name')
#    user_type = request.data.get('user_type')
#    phone_number = request.data.get('phone_number')
#    user_name = request.data.get('email')
#    password = request.data.get('password')

#    if name and last_name and user_type and phone_number and user_name and password:
#        user = User.objects.create_usercreate_user(user_name=user_name, password=password, name=name, last_name=last_name, user_type=user_type, phone_number=phone_number)

#        return Response({'message': 'Usuario creado exitosamente'}, status=201)
#    else:
#        return Response({'error': 'Datos incompletos'}, status=400)
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response

@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        # Agregar un registro de depuración para ver los datos recibidos
        print("Datos recibidos en la solicitud:")
        print(request.data)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Agregar un registro de depuración para ver los datos serializados
            print("Datos serializados:")
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def get_all_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)