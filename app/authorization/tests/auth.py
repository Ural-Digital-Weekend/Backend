from django.test import TestCase
from rest_framework.test import APIClient

from authorization.tests.helpers import create_test_user


class AuthTest(TestCase):
    def setUp(self) -> None:
        self.user = create_test_user()
        self.client = APIClient()
        self.routes = {
            "login": "/api/auth/login",
            "refresh": "/api/auth/refresh",
            "register": "/api/auth/register",
        }

    def login(self):
        return self.client.post(self.routes['login'], data={
            "username": self.user['username'],
            "password": self.user['password'],
        })

    def test_login(self):
        response = self.login()
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

    def test_refresh(self):
        refresh_token = self.login().data.get('refresh')
        response = self.client.post(self.routes['refresh'], data={
            "refresh": refresh_token,
        })

        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

    def test_register(self):
        response = self.client.post(self.routes['register'], data={
            "username": "NewTestUser",
            "email": 'testuser@mail.ru',
            "password": 'somepass123',
        })

        self.assertEqual(201, response.status_code)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())
