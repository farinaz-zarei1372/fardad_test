import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
class TestTokenApi:

    def test_bad_input_data_returns_400(self, api_client):
        response = api_client.post("/core/get_token/", {"username": "admin", "password": ""})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_token_correctly_returns_200(self, api_client):
        user = baker.make(User)
        response = api_client.post("/core/get_token/", {"username": user.username, "password": user.password})
        assert response.status_code == status.HTTP_200_OK
