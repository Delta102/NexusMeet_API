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
def get_user_by_id(request, user_id):
    user = UserPromotor.objects.get(id = user_id)

    serializer = UserPromotorSerializer(user)
    return Response(serializer.data)