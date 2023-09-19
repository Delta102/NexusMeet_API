from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

## -> USER - PROMOTOR
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def create_users(request):
    print("Datos recibidos en la solicitud:")
    print(request.data)
    
    nombre = request.data.get('nombre')
    apellido = request.data.get('apellido')
    tipoUser = request.data.get('tipoUser')
    email = request.data.get('email')
    password = request.data.get('password')

    if nombre and apellido:
        user = UserPromotor.objects.create_user(email=email, password=password, nombre=nombre, apellido=apellido, tipoUser=tipoUser)

        # Generar el token de acceso para el usuario recién creado
        token_serializer = MyTokenObtainPairSerializer(data={'email': email, 'password': password})
        token_serializer.is_valid(raise_exception=True)
        token_data = token_serializer.validated_data
        access_token = token_data['access']

        return Response({'message': 'Usuario creado exitosamente', 'access_token': access_token}, status=201)
    else:
        return Response({'error': 'Datos incompletos'}, status=400)

@api_view(['GET'])
def get_all_users(request):
    users = UserPromotor.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


## -> EVENTOS

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