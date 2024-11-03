from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.models import User
from src.serializers.user_serializer import UserSerializer


class UserView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        "id",
        "name",
    )
    ordering_fields = (
        "created_at",
        "updated_at",
    )

    def get_queryset(self):
        return User.objects.order_by("-created_at")
