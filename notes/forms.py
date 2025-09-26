from django import forms
from .models import Note

class AddNote(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','content']
