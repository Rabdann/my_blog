from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        password = make_password(validated_data.get("password"))
        validated_data["password"] = password
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PersonalCabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']
        read_only_fields = [
            "id",
            "is_superuser",
            "last_login",
            "is_staff",
            "is_active",
            "date_joined",
        ]
