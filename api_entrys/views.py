from django.shortcuts import render
from rest_framework.decorators import api_view

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from PIL import Image
import qrcode
import qrcode.image.pil
from io import BytesIO

from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *
from api_events.models import Event

# Create your views here.
@api_view(['POST'])
def create_entry(request):
    if request.method == 'POST':
        
        entry_data = request.data.copy()
        
        if not entry_data:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        event = getEvent(entry_data['event'])
        
        entry_data['price_total'] = str(float(entry_data['quantity']) * (event.entry_price))
        
        serializer = EntrySerializer(data=entry_data)
        
        if serializer.is_valid():
            serializer.save()
            entry = get_entry(serializer.instance.id)
            add_qr(entry)
            update_event_by_entry(event, entry_data['quantity'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_entry(entry_id):
    return Entry.objects.get(id = entry_id)

def add_qr(entry):
    data = 'quantity: ' + str(entry.quantity) + ' event_id: ' + str(entry.event_id) + ' user_id: ' + str(entry.user_id)
    qr_generator(data, entry)

def getEvent(event_id):
    return Event.objects.get(id = event_id)

def update_event_by_entry(event, quantity):
    event.capacity -= int(quantity)
    event.save()

def qr_generator(data, entry):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit = True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen en un buffer
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
        
    qr_size = qr_image.size[0]
    
    logo = Image.open('media/full_logo_white.png')
    logo = logo.resize((50, 50))
    
    logo_size = logo.size[0]
    x = (qr_size - logo_size) // 2
    y = (qr_size - logo_size) // 2
    
    qr_image.paste(logo, (x,y))
    
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    
    entry.image_qr.save(f'entry_qr_{entry.id}.png', ContentFile(buffer.getvalue()))
    entry.save()