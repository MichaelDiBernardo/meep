from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    spaghetti = serializers.CharField(required=True)
