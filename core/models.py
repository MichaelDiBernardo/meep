import uuid

from django.db import models
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    author = models.ForeignKey(User, models.SET_NULL, null=True)
    ref_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    date_added = models.DateTimeField(null=False)
