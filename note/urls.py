from django.urls import path
from .views import NoteView, DetailsView, NoteCreateView, NoteUpdateView, NoteDeleteView


urlpatterns = [
    path('notes', NoteView.as_view(), name='notes.list'),
    path('notes/<int:pk>', DetailsView.as_view(), name='notes.details'),
    path('notes/<int:pk>/edit', NoteUpdateView.as_view(), name='notes.edit'),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(), name='notes.delete'),
    path('notes/new', NoteCreateView.as_view(), name='notes.create')
]