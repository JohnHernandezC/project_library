from django import forms
from .models import *

class AutorForm (forms.ModelForm):
    class Meta:
        model=autor
        fields= '__all__'