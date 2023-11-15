from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from .models import *

# Create your tests here.
class UserPromotorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'user_type': 'Promotor',
            'phone_number': '123-456-7890',
            'address': '123 Main St',
            'date_of_birth': '1990-01-01',
            'profile_picture': 'profile/default.jpg',
        }
        self.user = UserPromotor.objects.create_user(**self.user_data)
        self.login_data = {
            'username': 'testuser',
            'password': 'password123',
        }

    def test_create_user_promotor(self):
        url = reverse('create_user_promotor')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #def test_update_user(self):
    #    url = reverse('update_user', args=[self.user.id])
    #    updated_data = {
    #        'username': 'updateduser',
    #        'phone_number': '987-654-3210',
    #    }
    #    response = self.client.put(url, updated_data, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    self.user.refresh_from_db()
    #    self.assertEqual(self.user.username, 'updateduser')
    #    self.assertEqual(self.user.phone_number, '987-654-3210')

    #def test_login_view(self):
    #    url = reverse('login_view')
    #    response = self.client.post(url, self.login_data, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)

    #def test_logout_view(self):
    #    url = reverse('logout_view')
    #    self.client.force_authenticate(user=self.user)
    #    response = self.client.post(url, {'token': 'some_token'}, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    #def test_get_current_user(self):
    #    url = reverse('get_current_user')
    #    self.client.force_authenticate(user=self.user)
    #    response = self.client.get(url)
    #    self.assertEqual(response.status_code, status.HTTP_200_OK)
    #    self.assertEqual(response.data['username'], self.user.username)

    def test_get_user_by_id(self):
        url = reverse('get_user_by_id', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        