from django.urls import path

from . import views

urlpatterns = [
    path("entry", views.JournalEntryView.as_view()),
]
