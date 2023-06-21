from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'created_at'] 
        # The array contains the fields that will be displayed in the form.
