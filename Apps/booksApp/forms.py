from django import forms
from .models import *

class autorForm (forms.ModelForm):
    class Meta:
        model=autor
        fields= '__all__'