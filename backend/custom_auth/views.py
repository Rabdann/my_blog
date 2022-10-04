from rest_framework import generics
from rest_framework import views
from rest_framework import response
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from custom_auth.serializers import RegisterSerializer, LoginSerializer, PersonalCabinetSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(
            username=serializer.data.get("username")
        )
        check_pass = check_password(serializer.data.get('password'), user.password)
        if check_pass:
            login(request, user)
            return response.Response(serializer.data)
        return response.Response('Некоректный пароль', status=400)


class LogoutAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        return response.Response(logout(request))
    

class PersonalCabinetAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = PersonalCabinetSerializer

    def get_object(self):
        obj = self.request.user
        return obj

