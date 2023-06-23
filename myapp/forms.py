from . models import *
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django import forms

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"

class EducationForm(ModelForm):

    class Meta:
        model = Education
        fields = "__all__"
        widgets = {'description': TinyMCE(attrs={'cols': 50, 'rows': 30})}
        



