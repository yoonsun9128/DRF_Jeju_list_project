from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTest(APITestCase):
    def setUp(self):
        self.data = {"username":"qwe123", "password":"qwe123"}
        self.user = User.objects.create_user("qwe123", "qwe123")

    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
        response = self.client.get(
            path = reverse('user_view'),
            HTTP_AUTHORIZATION = f"Bearer {access_token}"
            )
        self.assertEqual(response.data['username'], self.data['username'])