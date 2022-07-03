from django.contrib.auth.models import User
from rest_framework.test import APIClient


def get_auth_api_client(username, password):
    client = APIClient()
    resp = client.post("/api/auth/login", data={
        "username": username,
        "password": password
    })
    access_token = resp.data.get("access")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    return client


def create_test_user() -> dict:
    userdata = {
        "username": "testuser",
        "email": "testuser@mail.ru",
        "password": "testuser",
    }

    User.objects.create_user(
        username=userdata['username'],
        email=userdata['email'],
        password=userdata['password'],
    )

    return userdata
