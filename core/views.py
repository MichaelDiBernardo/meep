from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.services import JournalEntryRepo

from .commands import CreateJournalEntryCommand
from .serializers import JournalEntrySerializer


class JournalEntryView(APIView):
    def post(self, request):
        cmd = CreateJournalEntryCommand(journal_entry_repo=JournalEntryRepo())
        entry = cmd.run(request.user)
        serializer = JournalEntrySerializer(entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
