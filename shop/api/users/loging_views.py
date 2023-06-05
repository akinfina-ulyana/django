from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class LoginView(CreateAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = authenticate(request.POST["email"], request.POST["password"])
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get_or_create(user=user)[0].key
        return Response(status=status.HTTP_200_OK, data={"token": token})
