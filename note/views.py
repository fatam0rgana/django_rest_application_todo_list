from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Note
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


class DetailsView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'


class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'