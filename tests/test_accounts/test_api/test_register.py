import pytest
from django.core import mail
from django.urls import reverse
from rest_framework import status


class TestUserRegister:
    url = 'register'

    @pytest.mark.django_db
    def test_register(self, api_client, celery_fixture):
        response = api_client.post(reverse(self.url),
                                   data={'email': 'example@gmail.com',
                                         'user_name': 'testuser'})
        assert len(mail.outbox) == 1
        assert response.status_code == status.HTTP_201_CREATED
