from rest_framework import status
from rest_framework.response import Response as ResponseDRF


class Response(ResponseDRF):
    def __init__(self, data=None, status=status.HTTP_200_OK):
        super().__init__(None, status=status)

        self.data = {"data": data}
