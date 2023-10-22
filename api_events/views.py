from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
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
def get_event_by_id(request, event_id):
    event = Event.objects.get(id = event_id)

    serializer = EventSerializer(event)
    return Response(serializer.data)