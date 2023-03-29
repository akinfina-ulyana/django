import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestProductApi:
    def setup_method(self):
        self.client = APIClient()

    def test_my_function(self):
        response = self.client.get("/api/products/")
        assert response.status_code == 200