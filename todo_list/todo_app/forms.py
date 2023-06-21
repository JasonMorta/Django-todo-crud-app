from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo # The model that will be used to create the form
        fields = ['title', 'description'] 
        # The array contains the fields that will be displayed in the form.
