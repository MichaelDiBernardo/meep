from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import TestSerializer


class Spoof:
    def __init__(self):
        self.spaghetti = "cotto"


class HelloView(APIView):
    def get(self, request, format=None):
        serializer = TestSerializer(Spoof())
        return Response(serializer.data)
