import json
from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.datastructures import MultiValueDict
from django.http import QueryDict

from .views import *
from .models import *
from api.views import *
from api_events.views import *
from api.models import *
from api_events.models import *

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

class EntryTestCase(APITestCase):
    def setUp(self):
        self.user_promotor = UserPromotor.objects.create(id=1, user_type="promotor", username="promotor1", email="promotor1")

        self.event = Event.objects.create(
            creator=self.user_promotor,
            date_event_start="2023-10-25T12:00:00Z",
            event_image=SimpleUploadedFile("test_image.jpg", b"file_content"),
            event_name="Mi Evento de Prueba",
            description="Este es un evento de prueba.",
            capacity=100,
            entry_type="Gratis",
            entry_price=0.0,
        )

    def test_create_entry_successful(self):
        entry_data = {
            "event": self.event.id,
            "quantity": 2,
        }

        response = self.client.post("entrys/create/", entry_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Entry.objects.count(), 1)

    def test_create_entry_no_data(self):
        response = self.client.post("entrys/create/", {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_entry_no_event(self):
        entry_data = {
            "quantity": 2,
        }

        response = self.client.post("entrys/create/", entry_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


