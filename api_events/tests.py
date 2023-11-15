# from django.test import TestCase
# from django.http import QueryDict
# from rest_framework.test import APIRequestFactory
# from django.core.files.uploadedfile import SimpleUploadedFile

# from django.core.files import File
# import json
# from .models import *
# from .views import *


# # Create your tests here.
# class EventTestCase(TestCase):
#     def setUp(self):
#         self.user_promotor = UserPromotor.objects.create(id=10, user_type="promotor", username="promotor1")
        
#         with open("media/full_logo_black.png", "rb") as f:
#             file_content = f.read()
#             image_data = SimpleUploadedFile("test_image.jpg", file_content)
        
#         event_data = {
#             "creator": self.user_promotor.id,
#             "date_event_start": "2023-10-25T12:00:00Z",
#             "event_image": image_data,
#             "event_name": "Mi Evento de Prueba",
#             "description": "Este es un evento de prueba.",
#             "capacity": 100,
#             "entry_type": "Gratis",
#             "entry_price": 0.0,
#         }
#         event_data_querydict = QueryDict(mutable=True)
#         for key, value in event_data.items():
#             event_data_querydict.update({key: value})
    
#         self.event_data = event_data_querydict
        

#     def test_create_event(self):
#         factory = APIRequestFactory()
#         request = factory.post("events/create/", data=self.event_data, format="multipart")
#         response = create_event(request)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         self.assertEqual(Event.objects.count(), 1)

#     def test_get_event_by_id(self):
#         with open("media/full_logo_black.png", "rb") as f:
#             file_content = f.read()
#             image_data = SimpleUploadedFile("test_image.jpg", file_content)
            
#         event_data = {
#             "creator": self.user_promotor,
#             "date_event_start": "2023-10-25T12:00:00Z",
#             "event_image": image_data,
#             "event_name": "Mi Evento de Prueba",
#             "description": "Este es un evento de prueba.",
#             "capacity": 100,
#             "entry_type": "Gratis",
#             "entry_price": 0.0,
#         }
#         event = Event.objects.create(**event_data)        
#         factory = APIRequestFactory()
#         event = Event.objects.first()
#         event_id = event.id
    
#         request = factory.get(f"event/{event_id}/")
#         response = get_event_by_id(request, event_id=event_id)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         expected_data = EventSerializer(event).data
#         self.assertEqual(response.data, expected_data)
        
#     def test_get_all_events(self):
#         factory = APIRequestFactory()
#         request = factory.get('events/')
#         response = get_all_events(request)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         events = Event.objects.all()
#         expected_data = EventSerializer(events, many=True).data
#         self.assertEqual(response.data, expected_data)

#     def test_get_all_events_by_user(self):

#         user_id = 1
#         factory = APIRequestFactory()
#         request = factory.get(f'events-by-user/{user_id}/') 
#         response = get_all_events_by_user(request, user_id=user_id)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         events = Event.objects.filter(creator=user_id)
#         expected_data = EventSerializer(events, many=True).data
#         self.assertEqual(response.data, expected_data)