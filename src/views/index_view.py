from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from src.libraries.response import Response


class IndexView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return Response({"result": "Ping!!"})
