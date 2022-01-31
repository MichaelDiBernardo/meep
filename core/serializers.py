from http.client import SERVICE_UNAVAILABLE
from rest_framework import serializers
from .models import JournalEntry


class JournalEntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="ref_id")

    class Meta:
        model = JournalEntry
        fields = ["id", "date_added", "author"]
