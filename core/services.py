from django.utils import timezone
from .models import JournalEntry


class JournalEntryRepo:
    def create(self, author):
        return JournalEntry.objects.create(
            author=author,
            date_added=timezone.now(),
        )
