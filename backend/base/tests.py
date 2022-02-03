from django.test import TestCase
from django.urls import reverse
from .models import *
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


# Create your tests here.

class TestListCreateCustomer(APITestCase):
    def authenticate(self):
        token = Token.objects.get(user__username='abdulahio')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.data}")

    def testGetAllUser(self):
        
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
    
    def testRegisterUser(self):
        data = {
            'first_name':'lami',
            'last_name': 'oba',
            'email':'lami@gmail.com',
            'password':'lamipass',
            'phone_number':'09087654323',

        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def testWeatherAPI(self):
        data = {
            'lon':-2.34,
            'lat': 3.00,
        }
        response = self.client.post(reverse('get_weather'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def authUser(self):
        self.authenticate
        print(self.credentials)
        self.assertEqual(self.credentials, str)


    
