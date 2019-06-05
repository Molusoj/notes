from django import forms
from .models import Note


class NoteCreateForm(forms.ModelForm):
    class meta:
        model = Note
        fields = ('title', 'body')
