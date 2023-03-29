from django.test.client import Client

import pytest


@pytest.mark.django_db
class TestRegister:
    def setup_method(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        response = self.client.post("/register/", data={
            "first_name": "test",
            "last_name": "test",
            "email": "test@test.com",
            "password": "test@te",
            }, follow=True)