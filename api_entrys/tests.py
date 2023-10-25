from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .views import get_entrys_by_user, create_entry
from .models import Entry
from .serializers import EntrySerializer
from api_events.models import Event
from api.models import *
from .views import getEvent, get_entry, add_qr, update_event_by_entry
from django.contrib.auth.models import User

#class EntryViewsTestCase(TestCase):
    #def setUp(self):
        # Crea eventos y usuarios de prueba si es necesario
    #    self.user_promotor = UserPromotor.objects.create(id=10, user_type="promotor", username="promotor1")
    #    self.event = Event.objects.create(creator=self.user_promotor, date_event_start="2023-10-25T12:00:00Z", event_name="Mi Evento de Prueba", description="Este es un evento de prueba", capacity=100, entry_type="Gratis", entry_price=0.0)
    #    self.user = UserPromotor.objects.create_user(username="testuser", password="testpassword")
    
    #def test_get_entrys_by_user(self):
    #    factory = APIRequestFactory()
    #    user_id = self.user_promotor.id  # Cambia esto al ID del usuario de prueba
    #    request = factory.get(f'/entrys/get-entrys-by-user/{user_id}/')  # Asegúrate de que la URL coincida con la de tu vista
    #    response = get_entrys_by_user(request, user_id=user_id)

    #   self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    entries = Entry.objects.filter(user_id=user_id)
    #    expected_data = EntrySerializer(entries, many=True).data
    #    self.assertEqual(response.data, expected_data)

    #def test_create_entry(self):
    #    factory = APIRequestFactory()
    #    event_data = {'event': self.event.id, 'quantity': 2}  # Cambia esto según tus necesidades
    #    request = factory.post('/entrys/create/', data=event_data, format='json')  # Asegúrate de que la URL coincida con la de tu vista
    #    response = create_entry(request)

    #    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #    entry = Entry.objects.get(id=response.data['id'])
        
        # Realiza las aserciones necesarias para verificar que la entrada se creó correctamente
    #    self.assertEqual(entry.quantity, event_data['quantity'])
    #    self.assertEqual(entry.price_total, 2.0 * self.event.entry_price)  # Calcula el precio total esperado
    #    self.assertEqual(entry.event, self.event)
    #    self.assertEqual(entry.event_name, self.event.event_name)
