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
        

class Pro_skillForm(ModelForm):
    class Meta:
        model = Pro_skill
        fields = "__all__"
        widgets = {'name':forms.TextInput(attrs={'placeholder':'Enter pro skills'})}

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = "__all__"
        widgets = { 'name':forms.TextInput(attrs={'placeholder':'Enter language'})}



class Project_Form(ModelForm):

    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'description': TinyMCE(attrs={'cols':20, 'rows':20}),
            'name':forms.TextInput(attrs={'placeholder':'Enter project name '})
            }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"