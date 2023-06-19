from . models import *
from django.forms import ModelForm



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class HeroForm(ModelForm):
    class Meta:
        model = Hero
        fields = "__all__"

class AboutForm(ModelForm):
    class Meta:
        model = About
        fields ="__all__"

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"