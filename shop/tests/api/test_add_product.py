import pytest

from django.test.client import Client


@pytest.mark.django_db
class TestRegister:
    def setup_method(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        response = self.client.post(
            "/register/",
            data={
                "title": "test",
                "color": "test",
                "price": "test@test.com",
            },
            follow=True,
        )
