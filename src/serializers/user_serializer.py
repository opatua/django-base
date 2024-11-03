from rest_framework.serializers import ModelSerializer

from src.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class ReadUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "created_at",
            "updated_at",
            "last_login",
            "role",
        ]
