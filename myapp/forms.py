from . models import *
from django.forms import ModelForm


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"




