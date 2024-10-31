from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from src.exceptions.sign_in_validation_error import SignInValidationError
from src.serializers.user import ReadUserSerializer
from src.services.token_service import TokenService


class SignInView(APIView):
    permission_classes = [AllowAny]
    token_service = TokenService()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if not (email and password):
            raise SignInValidationError()

        user = authenticate(request, email=email, password=password)
        if not user:
            raise SignInValidationError()

        return Response(
            data={
                "data": {
                    "token": self.token_service.get_access_token(user),
                    "user": ReadUserSerializer(
                        user,
                    ).data,
                },
            },
            status=status.HTTP_200_OK,
        )
