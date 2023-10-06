from rest_framework.decorators import *
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
def create_user_promotor(request):
    if request.method == 'POST':
        user_promotor_data = request.data
        print("Datos del Promotor")
        print(user_promotor_data)
        
        password = user_promotor_data.get('password')
        print('Pass:' + password)
        user_promotor_data['password'] = make_password(password)
        print(user_promotor_data)
        user_promotor_serializer = UserPromotorSerializer(data=user_promotor_data)
        user_promotor_serializer.is_valid(raise_exception=True)
        
        user_promotor_serializer.save()
        return Response(user_promotor_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(user_promotor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        print(password+'hola')
        try:
            user = UserPromotor.objects.get(username=username)
            print(user)
            user = authenticate(request, username=username, password=password)
        except UserPromotor.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)

            # Generar un token de autenticación para el usuario
            token, created = Token.objects.get_or_create(user=user)

            # Devolver el token en la respuesta
            return Response({'token': token.key, 'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            # Verificar si el error se debe a un usuario no encontrado o una contraseña incorrecta
            try:
                user = UserPromotor.objects.get(username=username)
                return Response({'message': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
            except UserPromotor.DoesNotExist:
                return Response({'message': 'Nombre de usuario no encontrado'}, status=status.HTTP_401_UNAUTHORIZED)
            
            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    # Elimina el token de autenticación del usuario actual
    Token.objects.filter(user=request.user).delete()
    return Response({'message': 'Logout exitoso'}, status=status.HTTP_200_OK)


## -> EVENTOS

@api_view(['PUT'])
def update_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "El evento no existe."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, event_id):
    try:
        
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "El evento no existe."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    try:
        user_data ={
            'username': request.user.username,
            'id': request.user.id,
            'user_type': request.user.user_type,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    except UserPromotor.DoesNotExist:
        return Response({'error: El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)


        

@api_view(['GET'])
def get_all_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_all_events_by_user(request, user_id):
    events = Event.objects.filter(creator = user_id)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = UserPromotor.objects.get(id = user_id)

    serializer = UserPromotorSerializer(user)
    return Response(serializer.data)