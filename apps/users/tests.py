from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.users.models import User



class RegistrationTest(APITestCase):
    def setUp(self):
        self.register_url = reverse('registration')
        self.valid_payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'password_confirmation': 'testpassword',
        }

    def test_registration_success(self):
        response = self.client.post(
            self.register_url, self.valid_payload, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertTrue('refresh' in response.data)
        self.assertTrue('access' in response.data)

    def test_registration_failure(self):
        invalid_payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'password_confirmation': 'differentpassword',
        }
        response = self.client.post(
            self.register_url, invalid_payload, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )


class LoginTest(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword'
        )
        self.valid_payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }

    def test_login_success(self):
        response = self.client.post(
            self.login_url, self.valid_payload, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' in response.data)
        self.assertTrue('access' in response.data)

    def test_login_failure(self):
        invalid_payload = {
            'email': 'test@example.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(
            self.login_url, invalid_payload, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )


class ResetPasswordTest(APITestCase):
    def setUp(self):
        self.reset_password_url = reverse('reset_password')
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword'
        )
        self.valid_payload = {
            'email': 'test@example.com'
        }

    def test_reset_password_success(self):
        response = self.client.post(
            self.reset_password_url, self.valid_payload, format='json'
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_reset_password_unsuccess(self):
        self.invalid_payload = {
            'email': 'ass@example.com'
        }
        response = self.client.post(
            self.reset_password_url, self.invalid_payload, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )