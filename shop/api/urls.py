from api.products.views import ProductViewSet
from api.users.views import RegisterView
from rest_framework import routers

from django.urls import include, path

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("register_1/", RegisterView.as_view(), name="register_1"),
]
