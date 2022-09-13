from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .forms import NotesForm
from .serializers import NoteSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import isOwner


class NoteApiView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)


class NoteApiAddView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)


class NoteApiEditView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (isOwner,)


class NoteApiDeleteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (isOwner,)


class NoteView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/welcome.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.note.all()


class NoteCreateView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    success_url = '/'

    def get_queryset(self):
        return self.request.user.note.all()


class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/'

    def get_queryset(self):
        return self.request.user.note.all()
