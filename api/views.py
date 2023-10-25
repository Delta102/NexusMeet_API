from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .serializers import *
from .models import *



# -> USUARIOS API VIEWS:

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
        print(user_promotor_serializer.data)
        return Response(user_promotor_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(user_promotor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_user(request, id):
    try:
        user_promotor = UserPromotor.objects.get(id = pk)
    except UserPromotor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UserPromotor(user_promotor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = authenticate(username = username, password = password)
        
        if user is not None:
            login(request, user)
            #payload = jwt_payload_handler(user)
            #token = jwt_encode_handler(payload)
            return Response({'token': 'sadf', 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    # Invalida el token de acceso
    try:
        refresh_token = RefreshToken(request.data['token'])
        refresh_token.blacklist()  # Agrega el token a la lista negra para invalidarlo
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid token'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    print('Petición')
    user = request.user
    serializer = UserPromotorSerializer(user)
    return Response(serializer.data)



@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = UserPromotor.objects.get(id = user_id)

    serializer = UserPromotorSerializer(user)
    return Response(serializer.data)
    

#@api_view(['POST'])
#def add_attendee(request):
    #try:
        # Buscar el evento y el usuario en base a los IDs proporcionados en la URL
        #event = Event.objects.get(pk=event_id)
        #user = UserPromotor.objects.get(pk=user_id)

        # Agregar al usuario como asistente al evento
        #event.attendees.add(user)

        #return Response({'message': f'El usuario {user.username} ha sido agregado como asistente al evento {event.event_name}'}, status=status.HTTP_201_CREATED)
    #except Event.DoesNotExist:
        #return Response({'error': 'El evento no existe'}, status=status.HTTP_404_NOT_FOUND)
    #except UserPromotor.DoesNotExist:
        #return Response({'error': 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)