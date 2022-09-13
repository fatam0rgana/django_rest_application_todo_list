from django.urls import path
from .views import *


urlpatterns = [
    path('', NoteView.as_view(), name='note.list'),
    path('note/<int:pk>/edit', NoteUpdateView.as_view(), name='note.edit'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='note.delete'),
    path('note/new', NoteCreateView.as_view(), name='note.create'),
    path('api/notes', NoteApiView.as_view(), name='note.api_list'),
    path('api/notes/new', NoteApiAddView.as_view(), name='note.api_add'),
    path('api/notes/<int:pk>/edit', NoteApiEditView.as_view(), name='note.api_edit'),
    path('api/notes/<int:pk>/delete', NoteApiDeleteView.as_view(), name='note.api_delete')
]