from django import forms
from django.core.exceptions import ValidationError

from .models import Note


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        labels = {'title': 'Write your title here:', 'text': 'Write your text here:'}

    '''def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title:
            raise ValidationError('django')
        return title'''