from rest_framework_simplejwt.tokens import RefreshToken

from src.models import User


class TokenService:
    def get_access_token(self, user: User):
        refresh = self.get_refresh_token(user)
        return str(refresh.access_token)

    def get_refresh_token(self, user: User):
        return RefreshToken.for_user(user)
