from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
        return Response(user_promotor_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(user_promotor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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